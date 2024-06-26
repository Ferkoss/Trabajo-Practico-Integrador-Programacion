from abc import ABC, abstractmethod
from datetime import *
class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,apellido,fecha_nacimiento:date):
        self._nombre=nombre
        self._apellido=apellido
        self._fecha_nacimiento=fecha_nacimiento
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,new_nombre):
        self._nombre=new_nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,new_apellido):
        self._apellido=new_apellido

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @property
    def edad(self):
        if (date.today()>=self._fecha_nacimiento):
            return  date.today().year - self._fecha_nacimiento.year
        else:
            return (date.today().year - self._fecha_nacimiento.year)-1