from typing import Any

class StorageError(Exception):
    def __init__(self, message:str, *args) -> None:
        self.args = args
        super().__init__(message)

class Storage():
    _instance = None
    data = {}
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Storage, cls).__new__(cls)
        return cls._instance

    def set(self, key:str, value:Any) -> None:
        try:
            if key == '' or key == None or key == ' ':
                raise StorageError(
                    'Key.value: {}.\nNo puede ser None o un  STR vacio'
                )
            try:
                value = self.data[key]
                if value:
                    raise StorageError(
                        'Ya existe un objeto con el Key.value: {}\nCambia a .mut para cambiar el valor'.format(key)
                    )
            except KeyError as e:
                pass
            self.data.setdefault(
                key,
                value
            )
            return None
        except TypeError:
            print('Error: {}\nData: {}'.format(TypeError.__class__, TypeError.args))
            raise StorageError(
                'Key debe ser de tipo STR',
                ('key.value = {}'.format(key))
            )

        except ValueError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'Los parametros no son validos',
                ('Los parametros resivieron un valor in esperado')
            )

    def search(self, key:str) -> Any:
        try:
            value = self.data[key]
            return value
        except TypeError:
            print('Error: {}\nData: {}'.format(TypeError.__class__, TypeError.args))
            raise StorageError(
                'Key debe ser de tipo STR',
                ('key.value = {}'.format(key))
            )

        except ValueError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'Los parametros no son validos',
                ('Los parametros resivieron un valor in esperado')
            )

        except KeyError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'No existe Key asosiada a ningun valor',
                ('No existe Key.value: {} asosiada a ningun valor'.format(key))
            )

    def mut(self, key, value) -> None:
        try:
            validate = self.data[key]
            self.data[key] = value
            return None
        except TypeError:
            print('Error: {}\nData: {}'.format(TypeError.__class__, TypeError.args))
            raise StorageError(
                'Key debe ser de tipo STR',
                ('key.value = {}'.format(key))
            )

        except ValueError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'Los parametros no son validos',
                ('Los parametros resivieron un valor in esperado')
            )

        except KeyError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'No existe Key asosiada a ningun valor',
                ('No existe Key.value: {} asosiada a ningun valor'.format(key))
            )

    def delete(self, key):
        try:
            del self.data[key]
            return None
        except TypeError:
            print('Error: {}\nData: {}'.format(TypeError.__class__, TypeError.args))
            raise StorageError(
                'Key debe ser de tipo STR',
                ('key.value = {}'.format(key))
            )

        except ValueError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'Los parametros no son validos',
                ('Los parametros resivieron un valor in esperado')
            )

        except KeyError as e:
            print(f"Error: {e.__class__.__name__} - {e}")
            raise StorageError(
                'No existe Key asosiada a ningun valor',
                ('No existe Key.value: {} asosiada a ningun valor'.format(key))
            )