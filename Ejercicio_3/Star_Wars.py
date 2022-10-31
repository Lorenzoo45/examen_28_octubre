# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves y la debes de crear tu– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:
#  realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
# • mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# • determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# • indicar cuál es la nave que requiere mayor cantidad de tripulación;
# • mostrar todas las naves que comienzan con AT;
# • listar todas las naves que pueden llevar seis o más pasajeros;
# •  mostrar toda la información de la nave más pequeña y la más grande.



from audioop import reverse


class Nave():
    def __init__(self,nombre, largo, tripulación ,pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulación = tripulación
        self.pasajeros = pasajeros
    
    def __str__(self):
        return self.nombre + " " + str(self.largo) + " " + str(self.tripulación) + " " + str(self.pasajeros)
    #ordena las naves por nombre
def orden_nombres(lista):
    lista.sort(key=lambda nave: nave.nombre)
    return lista
def orden_largo(lista):
    lista.sort(key=lambda nave: nave.largo, reverse=True)
    return lista
def cinco_mayores(lista):
    lista.sort(key=lambda nave: nave.pasajeros)
    return lista[:5]


#nave con mayor tripulación
def mayor_tripulacion(lista):
    lista.sort(key=lambda nave: nave.tripulación, reverse=True)
    return lista[0]
#naves que empiezan con AT
def empieza_con_AT(lista):
    for nave in lista:
        if nave.nombre.startswith("AT"):
            print(nave)
#naves que pueden llevar 6 o más pasajeros
def seis_o_mas(lista):
    for nave in lista:
        if nave.pasajeros >= 6:
            print(nave)
#nave más pequeña y más grande
def nave_pequeña(lista):
    lista.sort(key=lambda nave: nave.largo)
    return str(lista[0])
def nave_grande(lista):
    lista.sort(key=lambda nave: nave.largo, reverse = True)
    return str(lista[0])





