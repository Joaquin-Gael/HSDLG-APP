import requests
from typing import Dict, Optional, List
from pydantic import EmailStr
from root import settings

class HttpClient:
    """
    Clase para realizar solicitudes HTTP con soporte para configuración de headers, cookies y hooks.

    Attributes:
        headers (Dict): Headers a enviar con cada solicitud.
        form (bool): Indica si los datos se envían como formulario.
        format_data (str): Formato de los datos (por defecto 'application/json').
        cookies (Dict): Cookies a enviar con cada solicitud.
        session (requests.Session): Sesión de requests para manejar las solicitudes.
        url (str): URL base de la API.
        endpoints (List[str]): Lista de endpoints específicos de la API.
        hooks_class (Optional[type]): Clase que maneja hooks personalizados.
        token (str): Token de autorización.
        full_url (str): URL completa construida a partir de la URL base y los endpoints.
    """

    def __init__(
            self,
            headers: Optional[Dict] = None,
            form: bool = False,
            format_data: str = 'application/json',
            cookies: Optional[Dict] = None,
            url: Optional[str] = None,
            endpoints: Optional[List[str]] = None,
            hooks_class: Optional[type] = None,
            token: Optional[str] = None
        ) -> None:
        """
        Inicializa la clase HttpClient.

        Args:
            headers (Optional[Dict]): Headers opcionales a enviar con las solicitudes.
            form (bool): Indica si los datos se envían como formulario.
            format_data (str): Formato de los datos (por defecto 'application/json').
            cookies (Optional[Dict]): Cookies opcionales a enviar con las solicitudes.
            url (Optional[str]): URL base de la API (por defecto, se usa el valor de settings.API_URL).
            endpoints (Optional[List[str]]): Lista de endpoints específicos de la API.
            hooks_class (Optional[type]): Clase que maneja hooks personalizados.
            token (Optional[str]): Token de autorización (por defecto, es una cadena vacía).
        """
        self.headers = headers or {}
        self.headers.setdefault('Content-Type', format_data)
        self.headers.setdefault('Authorization', f'Bearer {token}' if token else '')

        self.form = form
        self.cookies = cookies or {}
        self.session = requests.Session()
        self.url = settings.API_URL if url is None else url
        self.endpoints = endpoints or []
        self.hooks_class = hooks_class

        self.full_url = ''.join(f'{endpoint.rstrip("/")}/' for endpoint in self.endpoints)

    def set_endpoints(self, endpoints: Optional[List[str]] = None):
        """
        Establece los endpoints y actualiza la URL completa.

        Args:
            endpoints (Optional[List[str]]): Lista de nuevos endpoints a establecer.
        """
        self.endpoints = endpoints or []
        self.full_url = ''.join(f'{endpoint.rstrip("/")}/' for endpoint in self.endpoints)

    def get(self, retry: int, data: Optional[Dict] = None) -> Optional[requests.Response]:
        """
        Realiza una solicitud GET a la URL especificada.

        Args:
            retry (int): Número de reintentos en caso de error.
            data (Optional[Dict]): Datos a enviar con la solicitud.

        Returns:
            Optional[requests.Response]: Respuesta de la solicitud o None en caso de error.
        """
        data = data or {}

        try:
            response = self.session.get(
                self.full_url,
                data=data if self.form else None,
                json=None if self.form else data,
                hooks={'response': self.hooks_class.create_instance_orm} if self.hooks_class else None,
                allow_redirects=False
            )
            return response

        except requests.exceptions.HTTPError as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            raise self.HttpClientException(
                'Error: {}\nData: {}'.format(e.__class__, e.args)
            )

    def Auth(self, retry: Optional[int], dni: Optional[str], password: Optional[str], email: Optional[EmailStr]):
        """
        Método de autenticación usando el DNI y contraseña.

        Args:
            retry (int): Número de reintentos en caso de error.
            dni (str): DNI del usuario para autenticarse.
            password (str): Contraseña para autenticarse.

        Returns:
            Optional[requests.Response]: Respuesta de la autenticación o None en caso de error.
        """
        try:
            response = self.session.post(
                self.full_url,
                json={"dni": dni, "password": password} if dni is not None else {"email": email, "password": password},
                allow_redirects=False
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            raise self.HttpClientException(
                'Error: {}\nData: {}'.format(e.__class__, e.args)
            )
    
    class HttpClientException(Exception):
        def __init__(self, message:str, *args) -> None:
            self.args = args
            super().__init__(message)