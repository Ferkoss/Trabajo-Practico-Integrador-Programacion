from club import Club
from jugador import Jugador
from datetime import *
from dt import Dt
from liga import Liga
from pais import Pais
river = Club(
    nombre="Club Atlético River Plate",
    escudo="https://www.cariverplate.com.ar/wp-content/uploads/2022/09/Escudo-River-Plate-2022.png",
    presidente="Rodolfo D'Onofrio",
    plata=100000000,
    dt=Dt("Marcelo","Gallardo",date(1976,1,18),"4-4-2")
)

boca = Club(
    nombre="Club Atlético Boca Juniors",
    escudo="https://www.bocajuniors.com.ar/wp-content/uploads/2021/10/Escudo-Boca-Juniors-2021.png",
    presidente="Jorge Amor Ameal",
    plata=80000000,
    dt=Dt("Hugo","Ibarra", date(1974,4,1), "4-3-3")
)

newells = Club(
    nombre="Club Atlético Newell's Old Boys",
    escudo="https://www.newellsoldboys.com.ar/wp-content/uploads/2020/11/Escudo-Newells-2020.png",
    presidente="Ignacio Astore",
    plata=50000000,
    dt=Dt("Gabriel", "Heinze", date(1977,6,8), "4-4-2")
)

central = Club(
    nombre="Club Atlético Rosario Central",
    escudo="https://www.rosariocentral.com/imagenes/Escudo_Central.png",
    presidente="Gunnar Carl Nielsen",
    plata=60000000,
    dt=Dt("Carlos", "Tevez", date(1977,2,5), "3-4-3")
)




barcelona = Club(
    nombre="Fútbol Club Barcelona",
    escudo="https://www.cariverplate.com.ar/wp-content/uploads/2022/09/Escudo-River-Plate-2022.png",
    presidente="Joan Laporta i Estruch",
    plata=10000000000,
    dt=Dt("Hansi","Flick",date(1965,2,24),"4-4-2")
)

real_madrid = Club(
    nombre="Real Madrid Club de Fútbol",
    escudo="https://www.cariverplate.com.ar/wp-content/uploads/2022/09/Escudo-River-Plate-2022.png",
    presidente="Florentino Pérez",
    plata=10000000000,
    dt=Dt("Carlo","Ancelotti",date(1959,5,10),"4-3-3")
)

atlanta = Club(
    nombre = "Atlanta",
    escudo = "",
    presidente = "",
    plata = 50000000,
    dt=Dt("Valen", "Puto", date(1900,1,1),"Puto el que lee")

)





NOB_banega=Jugador("Ever","Banega",10,"Medio",90,85,1.9,date(1990,9,12))
NOB_cristian=Jugador("Cristian","Lema", 4, "Defensor", 82, 80, 184, date(1994, 3, 26))
NOB_facu=Jugador("Facundo","Mansur", 6, "Defensor", 77, 75, 183, date(1995, 2, 10))
NOB_wild=Jugador("Wilder","Rodríguez", 3, "Defensor", 80, 83, 181, date(1994, 10, 31))
NOB_garce=Jugador("Facundo","Garcé", 19, "Defensor", 78, 76, 186, date(1999, 3, 12))
NOB_perez=Jugador("Pablo","Pérez", 8, "Mediocampista", 84, 75, 178, date(1985, 8, 20))
NOB_bernardi=Jugador("Julián","Bernardi", 23, "Mediocampista", 86, 80, 172, date(1994, 6, 11))
NOB_maxi=Jugador("Maximiliano","Rodríguez", 10, "Mediocampista", 88, 75, 177, date(1984, 1, 2))
NOB_messi=Jugador("Leonel","Messi", 10, "Delantero", 100, 72,1.70, date(1984, 1, 2))
NOB_scocco=Jugador("Ignacio","Scocco", 9, "Delantero", 87, 83, 172, date(1985, 10, 10))
NOB_armani=Jugador("Brian","Aguirre", 17, "Delantero", 78,78, 1.70, date(2002, 11, 30))
NOB_cristaldo=Jugador("Jonatan","Cristaldo", 25, "Delantero",78.8, 70, 174, date(2002, 11, 30))

jugadores_newells = [NOB_banega,
NOB_cristian,
NOB_facu,
NOB_wild,
NOB_garce,
NOB_perez,
NOB_bernardi,
NOB_maxi,
NOB_messi,
NOB_scocco,
NOB_armani,
NOB_cristaldo]




for jugador in jugadores_newells:
    newells.add_jugadores(jugador)

newells.titulares=[NOB_messi,NOB_banega,NOB_maxi,NOB_scocco,NOB_bernardi]




# Lista de jugadores de Rosario Central (agregar más jugadores como sea necesario)

CEN_romero=Jugador("Gaspar","Romero", 1, "Arquero", 85.1, 80, 189, date(1994, 3, 20))
CEN_almada=Jugador("Facundo","Almada", 8, "Mediocampista", 81.4, 72, 171, date(2002, 2, 21))
CEN_vecchio=Jugador("Emiliano","Vecchio", 5, "Mediocampista", 84.2, 75, 175, date(1985, 12, 6))
CEN_marinelli=Jugador("Alan","Marinelli", 2, "Defensor", 80.5, 78, 185, date(1994, 10, 30))
CEN_mansur=Jugador("Facundo","Mansur", 6, "Defensor", 77.8, 75, 183, date(1995, 2, 10))
CEN_tancredi=Jugador("Mateo","Tancredi", 30, "Defensor", 79.2, 73, 184, date(2002, 4, 9))
CEN_covea=Jugador("Michael","Covea", 20, "Mediocampista", 82.1, 77, 178, date(1992, 7, 13))
CEN_rod_vecchio=Jugador("Rodrigo","Vecchio", 11, "Delantero", 78.4, 73, 172, date(1991, 3, 30))
CEN_gamba=Jugador("Luca","Gamba", 18, "Delantero", 80.7, 74, 176, date(2001, 10, 28))
CEN_osorio=Jugador("Jhonny","Osorio", 8, "Mediocampista", 83.5, 78, 174, date(1991, 5, 14))
CEN_russo=Jugador("Facundo","Russo", 15, "Defensor", 81.9, 78, 174, date(1991, 5, 14))

jugadores_central = [
CEN_romero,
CEN_almada,
CEN_vecchio,
CEN_marinelli,
CEN_mansur,
CEN_tancredi,
CEN_covea,
CEN_rod_vecchio,
CEN_gamba,
CEN_osorio,
CEN_russo
]

for jugador in jugadores_central:
    central.add_jugadores(jugador)



BOCA_rossi = Jugador("Agustín","Rossi", 1, "Arquero", 86.2, 80, 189, date(1995, 1, 21))
BOCA_advincula = Jugador("Luis","Advíncula", 2, "Defensor", 81.7, 73, 176, date(1991, 2, 2))
BOCA_izquierdoz = Jugador("Carlos","Izquierdoz", 24, "Defensor", 85.1, 86, 189, date(1988, 1, 30))
BOCA_rojo = Jugador("Marcos","Rojo", 16, "Defensor", 83.8, 78, 185, 24, date(1995,2, 20))
BOCA_fabra = Jugador("Frank","Fabra", 18, "Defensor", 81.5, 79, 177, 25, date(1992,6, 2))
BOCA_varela = Jugador("Alan","Varela", 23, "Mediocampista", 82.3, 78, 179, date(2001, 5, 4))
BOCA_pol_fernandez = Jugador("Guillermo Pol","Fernández", 5, "Mediocampista", 84.8, 79, 174, date(1991, 11, 4))
BOCA_payero = Jugador("Martín","Payero", 33, "Mediocampista", 82.9, 77, 179, date(2000, 7, 7))
BOCA_villa = Jugador("Sebastián","Villa", 22, "Delantero", 85.5, 75, 173, date(1995, 5, 4))
BOCA_benedetto = Jugador("Darío","Benedetto", 9, "Delantero", 84.9, 82, 186, date(1991,1,21))

jugadores_boca=[BOCA_rossi,
BOCA_advincula,
BOCA_izquierdoz,
BOCA_rojo,
BOCA_fabra,
BOCA_varela,
BOCA_pol_fernandez,
BOCA_payero,
BOCA_villa,
BOCA_benedetto]

for jugador in jugadores_boca:
    boca.add_jugadores(jugador)


RIVER_armani=Jugador("Franco","Armani", 1, "Arquero", 90, 80, 186, date(1986, 10, 13))
RIVER_quarta=Jugador("Milton","Casco", 4, "Defensor", 82.4, 75, 178, date(1992, 11, 11))
RIVER_martinez=Jugador("Javier","Pinola", 23, "Defensor", 84.5, 85, 187, date(1988, 4, 1))
RIVER_diaz=Jugador("Enzo","Díaz", 20, "Defensor", 83.2, 80, 180, date(1997, 3, 17))
RIVER_rojas=Jugador("Milton","Rojas", 26, "Defensor", 81.9, 78, 174, date(2002, 1, 26))
RIVER_ponce=Jugador("Bruno","Zuculini", 5, "Mediocampista", 82.7, 80, 178, date(1989, 6, 9))
RIVER_paradigma=Jugador("Enzo","Pérez", 24, "Mediocampista", 84.3, 82, 174, date(1986, 12, 22))
RIVER_de_la_cruz=Jugador("Nicolas","de la Cruz", 13, "Mediocampista", 87.1, 78, 180, date(1997, 6, 1))
RIVER_simon=Jugador( "Matías","Suárez", 7, "Delantero", 84.7, 78, 174, date(1988, 12, 23))
RIVER_beltran=Jugador("Julián","Álvarez", 9, "Delantero", 85.9, 75, 175, date(2000, 10, 31))
RIVER_alvarez=Jugador("Lucas","Beltrán", 19, "Delantero", 83.4, 75, 181, date(1996, 4, 30))

jugadores_river=[RIVER_armani,
RIVER_quarta,
RIVER_martinez,
RIVER_diaz,
RIVER_rojas,
RIVER_ponce,
RIVER_paradigma,
RIVER_de_la_cruz,
RIVER_simon,
RIVER_beltran,
RIVER_alvarez]

for jugador in jugadores_river:
    river.add_jugadores(jugador)


BARSA_ters_tegen = Jugador("Marc-André ter Stegen", 1, "Arquero", 93.7, 78, 187, 1, date(1992, 4, 30))
BARSA_dest = Jugador("Sergiño","Dest", 2, "Defensor", 83.3, 78, 175, 2, date(2000, 11, 24))
BARSA_araujo = Jugador("Ronald","Araujo", 3, "Defensor", 87.1, 86, 192, 3, date(1999, 3, 7))
BARSA_garcia = Jugador("Eric","Garcia", 23, "Defensor", 82.7, 79, 178, 4, date(2001, 1, 20))
BARSA_alba = Jugador("Jordi","Alba", 18, "Defensor", 85.8, 79, 170, 5, date(1989, 3, 21))
BARSA_busquets = Jugador("Sergio","Busquets", 5, "Mediocampista", 90.1, 80, 181, 6, date(1988, 7, 16))
BARSA_pedri = Jugador("Pedri", 8, "Mediocampista", 88.3, 74, 174, 7, date(2002, 11, 5))
BARSA_gavi = Jugador("Gavi","Gavira", 30, "Mediocampista", 84.9, 72, 173, 8, date(2004, 8, 5))
BARSA_dembele = Jugador("Ousmane","Dembélé", 11, "Delantero", 84.5, 75, 178, 9, date(1997, 2, 20))
BARSA_aubameyang = Jugador("Pierre Emerick","Aubameyang", 9, "Delantero", 87.3, 76, 181, 10, date(1989, 6, 1))
BARSA_ferran = Jugador("Ansu","Fati", 10, "Delantero", 84.2, 70, 178, 11, date(2002, 10, 31))

jugadores_barsa=[BARSA_ters_tegen,
BARSA_dest,
BARSA_araujo,
BARSA_garcia,
BARSA_alba,
BARSA_busquets,
BARSA_pedri,
BARSA_gavi,
BARSA_dembele,
BARSA_aubameyang,
BARSA_ferran]

for jugador in jugadores_barsa:
    barcelona.add_jugadores(jugador)


REAL_courtois = Jugador("Thibaut","Courtois", 1, "Arquero", 94.2, 80, 199, date(1992, 5, 11))
REAL_carvajal = Jugador("Dani"," Carvajal", 2, "Defensor", 85.7, 78, 173, date(1992, 7, 16))
REAL_militao = Jugador("Eder","Militao", 3, "Defensor", 87.5, 85, 186, date(2001, 2, 2))
REAL_alab = Jugador("David","Alaba", 4, "Defensor", 90.1, 81, 185, date(1991, 6, 27))
REAL_nach = Jugador("Nacho","Fernández", 6, "Defensor", 85.4, 81, 180, date(1993, 1, 27))
REAL_mendy = Jugador("Ferland","Mendy", 23, "Defensor", 85.1, 81, 178, date(1995, 6, 1))
REAL_rudiger = Jugador("Antonio","Rudiger", 22, "Defensor", 88.7, 85, 190, date(1993, 3, 3))
REAL_cassemiro = Jugador("Carlos","Casemiro", 14, "Mediocampista", 88.9, 80, 185, date(1992, 2, 23))
REAL_kroos = Jugador("Toni","Kroos", 8, "Mediocampista", 92.2, 78, 183, date(1990, 1, 3))
REAL_modric = Jugador("Luka","Modrić", 10, "Mediocampista", 91.3, 78, 178, date(1985, 9, 17))
REAL_camavinga = Jugador("Eduardo","Camavinga", 25, "Mediocampista", 84.3, 78, 182, date(2002, 10, 10))
REAL_valverde = Jugador("Federico","Valverde", 15, "Mediocampista", 86.9, 80, 183, date(1998, 7, 22))
REAL_tchouameni = Jugador("Aurélien","Tchouaméni",18,"Mediocampista", 86.9, 80, 183,date(2000,1,27))

jugadores_real=[REAL_courtois,
REAL_carvajal,
REAL_militao,
REAL_alab,
REAL_nach,
REAL_mendy,
REAL_rudiger,
REAL_cassemiro,
REAL_kroos,
REAL_modric,
REAL_camavinga,
REAL_valverde,
REAL_tchouameni]

for jugador in jugadores_real:
    real_madrid.add_jugadores(jugador)












argentina=Pais("Argentina","")
españa=Pais("España","")



primera_division_argentina=Liga("Primera División")
primera_division_españa=Liga("La Liga")

primera_division_argentina.add_equipos(newells)
primera_division_argentina.add_equipos(central)
primera_division_argentina.add_equipos(river)
primera_division_argentina.add_equipos(boca)

primera_division_españa.add_equipos(real_madrid)
primera_division_españa.add_equipos(barcelona)

argentina.add_liga(primera_division_argentina)
españa.add_liga(primera_division_españa)

lista_paises=[argentina,españa]
