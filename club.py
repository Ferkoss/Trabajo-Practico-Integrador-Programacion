from jugador import Jugador
from dt import Dt

class Club():
    def __init__(self,nombre,escudo,presidente,plata,dt:Dt):
        self.__nombre=nombre
        self.__escudo=escudo
        self.__presidente=presidente
        self.__plata=plata
        self.__jugadores=[]
        self.__titulares=[]
        self.__dt=dt

    @property 
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre=new_nombre

    @property
    def escudo(self):
        return self.__escudo
    @escudo.setter
    def escudo(self,new_escudo):
        self.__escudo=new_escudo

    @property
    def presidente(self):
        return self.__presidente
    @presidente.setter
    def presidente(self,new_presidente):
        self.__presidente=new_presidente

    @property
    def plata(self):
        return self.__plata
    @plata.setter
    def plata(self,new_plata):
        self.__plata=new_plata

    @property
    def dt(self):
        return self.__dt
    @dt.setter
    def dt(self,new_dt):
        self.__dt=new_dt

    @property
    def jugadores(self):
        return self.__jugadores
    def add_jugadores(self,jugador):
        self.__jugadores.append(jugador)

    def remove_jugadores(self,jugador):
        self.__jugadores.remove(jugador)

    def comprar_jugadores(self,jugador:Jugador):
        if self.__plata-jugador.valor<0:
            raise Exception("Dinero Insuficiente")
        self.add_jugadores(jugador)
        self.__plata-=jugador.valor

    def vender_jugadores(self,jugador:Jugador):
        self.remove_jugadores(jugador)
        self.__plata+=jugador.valor

    def cambio_titulares(self,entra:Jugador,sale:Jugador):
        self.__titulares.remove(sale)
        self.__titulares.append(entra)

    def __str__(self):
        return f"Club: {self.__nombre} Fondos: ${self.__plata}"
    
    

    @property
    def titulares(self):
        return self.__titulares
    
    @titulares.setter
    def titulares(self,new_titulares):
        self.__titulares=new_titulares
    
    
    