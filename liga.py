from club import Club

class Liga():
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__equipos=[]

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre=new_nombre

    @property
    def equipos(self):
        return self.__equipos

    @property
    def cantidad_equipos(self):
        return len(self.__equipos)
    
    def __str__(self):
        return f"Nombre: {self.__nombre} Cantidad de Equipos: {self.cantidad_equipos}"

    def add_equipos(self,equipo):
        self.__equipos.append(equipo)

    def remove_equipos(self,equipo):
        self.__equipos.remove(equipo)