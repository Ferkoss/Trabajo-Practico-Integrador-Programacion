from persona import Persona
from random import randrange

class Jugador(Persona):
    __lista_id=[]
    def __init__(self,nombre,apellido,dorsal,posicion,puntos_habilidad,peso,altura,fecha_nacimiento,tipo_lesion=None):
        self.__dorsal=dorsal
        self.__posicion=posicion
        self.__puntos_habilidad=puntos_habilidad
        self.__tipo_lesion=tipo_lesion
        self.__peso=peso
        self.__altura=altura
        self.__id=Jugador.__generar_id()
        super().__init__(nombre,apellido,fecha_nacimiento)

    @property
    def dorsal(self):
        return self.__dorsal
    @dorsal.setter
    def dorsal(self,new_dorsal):
        self.__dorsal=new_dorsal
    
    @property
    def posicion(self):
        return self.__posicion
    @posicion.setter
    def posicion(self,new_posicion):
        self.__posicion=new_posicion

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    @puntos_habilidad.setter
    def puntos_habilidad(self,new_puntos_habilidad):
        self.__puntos_habilidad=new_puntos_habilidad

    @property
    def tipo_lesion(self):
        return self.__tipo_lesion
    @tipo_lesion.setter
    def tipo_lesion(self,new_tipo_lesion):
        self.__tipo_lesion=new_tipo_lesion
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self,new_peso):
        self.__peso=new_peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self,new_altura):
        self.__altura=new_altura

    @property
    def id(self):
        return self.__id



    @property
    def valor(self):
        precio_inicial=float(100000)
        porcentaje=0
        if self.edad<=22:
            porcentaje+=0.50
        elif self.edad<30:
            porcentaje+=0.25
        
        if self.__puntos_habilidad>=70 and self.__puntos_habilidad<80:
            porcentaje+=0.1
        elif self.__puntos_habilidad>=80 and self.__puntos_habilidad<90:
            porcentaje+=0.15
        elif self.__puntos_habilidad>=90:
            porcentaje+=0.3

        if self.__tipo_lesion=="desgarre":
            porcentaje-=0.3
        
        elif self.__tipo_lesion=="fractura":
            porcentaje-=0.6
        
        return precio_inicial+precio_inicial*porcentaje
        

    def entrenar(self):
        self.__puntos_habilidad+=1

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Dorsal: {self.__dorsal} |Edad: {self.edad} Años | Valor: ${self.valor}"

    @classmethod
    def __generar_id(cls):
        id=randrange(1,1000) 
        while id in cls.__lista_id:
            id=randrange(1,1000)
        cls.__lista_id.append(id)
        return id
    
