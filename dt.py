from persona import Persona
from datetime import *
class Dt(Persona):
    def __init__(self,nombre,apellido,fecha_nacimiento, formacion_predeterminada):
        self.__formacion_predeterminada = formacion_predeterminada
        super().__init__(nombre, apellido, fecha_nacimiento)

    @property
    def formacion_predeterminada(self) -> str:
        return self.__formacion_predeterminada

    @formacion_predeterminada.setter
    def formacion_predeterminada(self, nueva_formacion) -> None:
        self.__formacion_predeterminada = nueva_formacion

    def __str__(self) -> str:
        return f"{self.formacion_predeterminada}"        