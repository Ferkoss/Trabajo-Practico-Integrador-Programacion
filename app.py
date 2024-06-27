from datos import *
from club import Club
from jugador import Jugador
from datetime import *
from dt import Dt
from liga import Liga
from pais import Pais
from random import randrange

def creacion_opciones(lista):
    opc=int(input("Ingrese su opcion: "))
    while opc<0 or opc>len(lista):
        opc=int(input("Ingrese su opcion nuevamente: "))
    return opc-1

def busca_equipo():
    print("Ingrese el pais del equipo")
    for i,pais in enumerate(lista_paises,1):
        print(str(i)+" - "+pais.nombre)
    pais_seleccionado=lista_paises[creacion_opciones(lista_paises)]


    print("Ingrese la liga del equipo")
    for i,liga in enumerate(pais_seleccionado.ligas,1):
        print(str(i)+" - "+liga.nombre)

    liga_seleccionada=pais_seleccionado.ligas[creacion_opciones(pais_seleccionado.ligas)]

    print("Ingrese el equipo")
    for i,equipo in enumerate(liga_seleccionada.equipos,1):
        print(str(i)+" - "+equipo.nombre)

    return liga_seleccionada.equipos[creacion_opciones(liga_seleccionada.equipos)]




def comprar_jugador(equipo_seleccionado):

    equipo_vendedor=busca_equipo()

    if equipo_vendedor==equipo_seleccionado:
        raise Exception("No podes comprar a tus propios jugadores")

    for i,jugadores in enumerate(equipo_vendedor.jugadores,1):
        print(str(i)+" - "+str(jugadores))

    jugador_comprado=equipo_vendedor.jugadores[creacion_opciones(equipo_vendedor.jugadores)]

    equipo_seleccionado.comprar_jugadores(jugador_comprado)
    equipo_vendedor.vender_jugadores(jugador_comprado)

    print("El jugador "+jugador_comprado.nombre+" "+jugador_comprado.apellido+" Perteneciente al club "+equipo_vendedor.nombre+" ha sido comprado por "+equipo_seleccionado.nombre)



def vender_jugador(equipo_seleccionado):

    print("Seleccione el jugador a vender")

    for i,jugador in enumerate(equipo_seleccionado.jugadores,1):
        print(str(i)+" - "+str(jugador))

    jugador_vendido=equipo_seleccionado.jugadores[creacion_opciones(equipo_seleccionado.jugadores)]

    equipo_comprador=busca_equipo()

    equipo_comprador.comprar_jugadores(jugador_vendido)
    equipo_seleccionado.vender_jugadores(jugador_vendido)

    print("El jugador "+jugador_vendido.nombre+" "+jugador_vendido.apellido+" Perteneciente a "+equipo_seleccionado.nombre+" ha sido comprado por "+equipo_comprador.nombre)



def ver_jugadores(equipo_seleccionado):
    for jugador in equipo_seleccionado.jugadores:
        print(jugador)
    



def cambio_titulares(equipo_seleccionado):
    for i,jugador in enumerate(equipo_seleccionado.titulares,1):
        print(str(i)+" - "+jugador.nombre+" "+jugador.apellido)
    

    
    

    jugador_sale=equipo_seleccionado.titulares[creacion_opciones(equipo_seleccionado.titulares)]
    suplentes=list(filter(lambda x:x not in equipo_seleccionado.titulares,equipo_seleccionado.jugadores))
    for i,jugador in enumerate(suplentes,1):
        print(str(i)+" - "+jugador.nombre+" "+jugador.apellido)

    

    jugador_entra=suplentes[creacion_opciones(suplentes)]
    equipo_seleccionado.cambio_titulares(jugador_entra,jugador_sale)
    print("Sale "+jugador_sale.nombre+" "+jugador_sale.apellido+" y entra "+jugador_entra.nombre+" "+jugador_entra.apellido)


def entrenar(equipo_seleccionado):

    jugadores_sin_lesion=list(filter(lambda x: not x.tipo_lesion,equipo_seleccionado.jugadores))

    for i,jugador in enumerate(jugadores_sin_lesion,1):
        
        print(str(i)+" - "+str(jugador.nombre)+" "+str(jugador.apellido)+" Puntos de habilidad: "+str(jugador.puntos_habilidad))

    jugador_entreado=jugadores_sin_lesion[creacion_opciones(jugadores_sin_lesion)]

    probabilidad_lesion=randrange(1,100) #La funcion randrange elije un numero al azar entre 1 y 100
                                         #si el numero esta entre 1 y 5 el jugador tuvo un desgarre
                                         #entre 5 y 10 tuvo una fractura, sino, entreno bien y sube puntos
    if probabilidad_lesion<=5:
        jugador_entreado.tipo_lesion="desgarre"
        print("El jugador "+jugador_entreado.nombre+" "+jugador_entreado.apellido+" ha sufrido un desgarre")
    elif probabilidad_lesion<=10:
        jugador_entreado.tipo_lesion="fractura"
        print("El jugador "+jugador_entreado.nombre+" "+jugador_entreado.apellido+" ha sufrido una fractura")
    else:
        jugador_entreado.entrenar()
        print("El jugador "+jugador_entreado.nombre+" "+jugador_entreado.apellido+" ahora tiene "+str(jugador_entreado.puntos_habilidad)+" puntos de habilidad")
    

def ver_lesionados(equipo_seleccionado):
    for jugador in equipo_seleccionado.jugadores:
        if jugador.tipo_lesion:
            print(jugador.nombre+" "+jugador.apellido+" Tipo Lesion: "+jugador.tipo_lesion)


def elegir_club():

    equipo_seleccionado=busca_equipo()

    print(equipo_seleccionado.escudo)

    while True:
        print("1. Cambiar titulares")
        print("2. Comprar Jugador")
        print("3. Vender Jugador")
        print("4. Ver mis jugadores")
        print("5. Ver Titulares")
        print("6. Entrenar Jugador")
        print("7. Ver jugadores Lesionados")
        print("8. Salir")
        opc=int(input("Ingrese su opcion: "))

        if opc==1:
            cambio_titulares(equipo_seleccionado)


        elif opc==2:
            comprar_jugador(equipo_seleccionado)
        elif opc==3:
            vender_jugador(equipo_seleccionado)
        elif opc==4:
            ver_jugadores(equipo_seleccionado)
        elif opc==5:
            for titular in equipo_seleccionado.titulares:
                print(titular)
        elif opc==6:
            entrenar(equipo_seleccionado)
        elif opc==7:
            ver_lesionados(equipo_seleccionado)
        elif opc==8:
            break
        else:
            print("opcion invalida")



def crear_jugador():
    nombre=input("Ingrese el nombre del jugador\n")
    apellido=input("Ingrese el apellido del jugador\n")
    dorsal=input("Ingrese su dorsal\n")

    print("Ingrese su pocisión")
    print("1.Portero - 2.Defensor - 3.Mediocampista - 4.Delantero")

    posicion=int(input("Ingrese su opcion: "))

    while posicion<1 or posicion>4:
        posicion=int(input("Ingrese su opcion nuevamente: "))

    if posicion==1:
        posicion="Portero"  
    elif posicion==2:
        posicion="Defensor" 
    elif posicion==3:
        posicion="Mediocampista"
    else:
        posicion="Delantero"

    peso=int(input("Ingrese el peso del jugador\n"))
    altura=float(input("Ingrese la altura del jugador\n"))

    fecha_nacimiento=input("Ingrese la fecha de nacimiento en formato DD/MM/AAAA\n")
    fecha_nacimiento=date(int(fecha_nacimiento[6:10]),int(fecha_nacimiento[3:5]),int(fecha_nacimiento[0:2]))

    print("Ingrese al equipo al cual va a pertenecer")
    equipo_jugador=busca_equipo()

    jugador_nuevo=Jugador(nombre,apellido,dorsal,posicion,60,peso,altura,fecha_nacimiento)
    equipo_jugador.add_jugadores(jugador_nuevo)
    print("Jugador agregado correctamente")






print(ascii_messi)
print(fifa_ascii)

while True:
    print("1. Elegir Club")
    print("2. Crear Jugador")
    print("3. Mostrar Clubes por nivel economico")
    print("4. Salir")
    opc=int(input("Ingrese su opcion: "))

    if opc==1:
        elegir_club()
    elif opc==2:
        crear_jugador()
    elif opc==3:

        for i,equipo in enumerate(sorted(lista_equipos,key=lambda x:x.plata, reverse=True),1):
            print(str(i)+" - "+str(equipo))

    elif opc==4:
        break
    else:
        print("opcion invalida")




print(gracias_ascii)
