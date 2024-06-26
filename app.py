from datos import *
from club import Club
from jugador import Jugador
from datetime import *
from dt import Dt
from liga import Liga
from pais import Pais





def elegir_club():

    for i,pais in enumerate(lista_paises,1):
        print(str(i)+" - "+pais.nombre)

    opc_pais=int(input("Ingrese su opcion: "))

    while opc_pais<0 or opc_pais>len(lista_paises):
        opc_pais=int(input("Ingrese su opcion nuevamente: "))

    pais_seleccionado=lista_paises[opc_pais-1]

    

    for i,liga in enumerate(pais_seleccionado.ligas,1):
        print(str(i)+" - "+liga.nombre)

    
    opc_liga=int(input("Ingrese su opcion: "))

    while opc_liga<0 or opc_liga>len(pais_seleccionado.ligas):
        opc_liga=int(input("Ingrese su opcion nuevamente: "))

    liga_seleccionada=pais_seleccionado.ligas[opc_liga-1]





    for i,equipo in enumerate(liga_seleccionada.equipos,1):
        print(str(i)+" - "+equipo.nombre)
    
    opc_equipo=int(input("Ingrese su opcion nuevamente: "))

    while opc_equipo<0 or opc_equipo>len(liga_seleccionada.equipos):
        opc_equipo=int(input("Ingrese su opcion nuevamente: "))

    equipo_seleccionado=liga_seleccionada.equipos[opc_equipo-1]
    
    



    while True:
        print("1. Cambiar titulares")
        print("2. Comprar Jugador")
        print("3. Vender Jugador")
        print("4. Ver mis jugadores")
        print("5. Salir")
        opc=int(input("Ingrese su opcion: "))

        if opc==1:
            for i,jugador in enumerate(equipo_seleccionado.titulares,1):
                print(str(i)+" - "+jugador.nombre+" "+jugador.apellido)

            opc_sale=int(input("Ingrese su opcion: "))

            while opc_sale<0 or opc_sale>len(equipo_seleccionado.titulares):
                opc_sale=int(input("Ingrese su opcion nuevamente: "))

            jugador_sale=equipo_seleccionado.titulares[opc_sale-1]

            suplentes=list(filter(lambda x:x not in equipo_seleccionado.titulares,equipo_seleccionado.jugadores))
            for i,jugador in enumerate(suplentes,1):
                print(str(i)+" - "+jugador.nombre+" "+jugador.apellido)
            
            opc_entra=int(input("Ingrese su opcion: "))

            while opc_entra<0 or opc_entra>len(equipo_seleccionado.titulares):
                opc_entra=int(input("Ingrese su opcion nuevamente: "))



        elif opc==2:
            pass
        elif opc==3:
            pass
        elif opc==4:
            break
        else:
            print("opcion invalida")






while True:
    print("1. Elegir Club")
    print("2. Crear Jugador")
    print("3. Mostrar Clubes")
    print("4. Salir")
    opc=int(input("Ingrese su opcion: "))

    if opc==1:
        elegir_club()
    elif opc==2:
        pass
    elif opc==3:
        pass
    elif opc==4:
        break
    else:
        print("opcion invalida")



