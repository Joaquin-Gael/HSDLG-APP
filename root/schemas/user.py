from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from requests import Response


class UsuarioCliente(BaseModel):
    userID: int
    dni: str
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[date] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    is_active: bool
    date_joined: date
    last_login: Optional[date] = None
    last_logout: Optional[date] = None
    imagen_url: Optional[str] = None

    class Config:
        orm_mode = True
    
    @classmethod
    def create_instance_orm(cls, res:Response, *args, **kwargs):
        try:
            json_data = res.json()
            res.user = cls(**json_data)
            return res
        except Exception as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            res.user = None
            return res