#lanzador
import sys
from Ejercicio_3.Star_Wars import cinco_mayores, orden_largo
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_3")
from Star_Wars import *



#nos creamos todas las naves que vamos a usar
nave_1 = Nave("Halcón Milenario", 34.37, 4, 6)*
nave_2 = Nave("Estrella de la Muerte", 120000, 342953, 843342)
nave_3 = Nave("AT-AT", 20, 5, 40)
nave_4 = Nave("AT-ST", 2, 2, 0)
nave_5 = Nave("AT-TE", 5, 2, 0)
nave_6 = Nave("AT-PT", 3, 2, 0)
nave_7 = Nave("AT-AT Walker", 20, 5, 40)
listaNaves = [nave_1,nave_2,nave_3,nave_4,nave_5,nave_6,nave_7]


def pruebas():
    while True:
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1]  Ejercicio 3")
        print("[2] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        #--------1era_opcion--------#
        if opcion == "1":
            # print("\nComprobamos la funcion catalogar: ")
            # Vehiculos.catalogar(lista_vehiculos)
            print("\n Comprobamos el ejercicio de las naves: ")
            print("Ordenamos las naves por nombre: ")
            naves_ordenadas = orden_nombres(listaNaves)
            print(naves_ordenadas)
            print("Ordenamos las naves por el largo: ")
            naves_ordenadas2 = orden_largo(listaNaves)
            print(naves_ordenadas2)
            print("Eneseñamos las 5 mayores: ")
            naves_ordenadas3 = cinco_mayores(listaNaves)
            print(naves_ordenadas3)
            print("Mostramos la info del halcon milenario y de la estrella de la muerte: ")
            print(nave_1)
            print(nave_2)
            print("Mostramos la nave con mayor tripulacion: ")
            print()




            

        if opcion == '2':
            print("Saliendo...\n")
            break
input("\nPresiona ENTER para continuar...")


