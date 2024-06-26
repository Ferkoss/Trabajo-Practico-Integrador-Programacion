from liga import Liga

class Pais():
    def __init__(self,nombre,bandera):
        self.__nombre=nombre
        self.__bandera=bandera
        self.__ligas=[]

    @property 
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre=new_nombre
    
    @property
    def bandera(self):
        return self.__bandera
    @bandera.setter
    def bandera(self,new_bandera):
        self.__bandera=new_bandera

    @property
    def ligas(self):
        return self.__ligas
    
    def add_liga(self,liga):
        self.__ligas.append(liga)

    def remove_liga(self,liga):
        self.__ligas.remove(liga)