# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves y la debes de crear tu– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:
#  realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# • mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# • determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# • indicar cuál es la nave que requiere mayor cantidad de tripulación;
# • mostrar todas las naves que comienzan con AT;
# • listar todas las naves que pueden llevar seis o más pasajeros;
# •  mostrar toda la información de la nave más pequeña y la más grande.



class Nave():
    def __init__(self,nombre, largo, tripulación ,pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulación = tripulación
        self.pasajeros = pasajeros
    #ordena las naves por nombre
    def orden_nombres(self,lista):
    #la idea es hacer esto commo una pila
    
        


    def __str__(self):
        return self.nombre + " " + str(self.largo) + " " + str(self.tripulación) + " " + str(self.pasajeros)
#nos creamos todas las naves que vamos a usar
nave_1 = Nave("Halcón Milenario", 34.37, 4, 6)
nave_2 = Nave("Estrella de la Muerte", 120000, 342953, 843342)
nave_3 = Nave("AT-AT", 20, 5, 40)
nave_4 = Nave("AT-ST", 2, 2, 0)
nave_5 = Nave("AT-TE", 5, 2, 0)
nave_6 = Nave("AT-PT", 3, 2, 0)
nave_7 = Nave("AT-AT Walker", 20, 5, 40)
listaNaves = [nave_1,nave_2,nave_3,nave_4,nave_5,nave_6,nave_7]
