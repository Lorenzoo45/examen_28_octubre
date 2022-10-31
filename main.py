#lanzador
import sys
from Ejercicio_2.matriz import SarrusI, SarrusR
from Ejercicio_3.Star_Wars import cinco_mayores, orden_largo
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_3")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_1")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_2")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_4")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_5")
from Star_Wars import *
from Hanoi import *
from matriz import *
from TDA import *
from desciptar import *
from cifrar import *
from hash import *




#nos creamos todas las naves que vamos a usar
nave_1 = Nave("Halcón Milenario", 34.37, 4, 6)
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
        print("[1] Ejercicio 1")
        print("[2] Ejercicio 2")
        print("[3]  Ejercicio 3")
        print("[4] Ejercicio 5")
        print("[5] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        if opcion == "1":
            print("Ejercicio donde aplicamos los movimientos de las torres de Hanoi de 3 discos sin utilizar tipos datos abstractos")
            print(moverTorre(3,"A","B","C"))
            print("Probamos ahora con 20 discos")
            print(moverTorre(20,"A","B","C"))
        if opcion == "2":
            print("Vamos a calcula el det. por el metodo de Sarrus Recursivo con la siguiente matriz:")
            matriz = [[6,2,60],[7,5,3],[7,7,1]]
            print(matriz)
            print(SarrusR(matriz))
            print("\n Ahora vamos a calcularlo por metodo iterativo con la matriz que tu quieras")
            print(SarrusI())

        #--------3era_opcion--------#
        if opcion == "3":
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
            print(mayor_tripulacion(listaNaves))
            print("Mostramos las naves cuyo nombre empieza por AT: ")
            print(empieza_con_AT(listaNaves))
            print("Mostramos las naves que tienen 6 o mas pasajeros: ")
            print(seis_o_mas(listaNaves))
            print("Mostramos la nave mas grande")
            print(nave_grande(listaNaves))
            print("Mostramos la nave mas pequeña")
            print(nave_pequeña(listaNaves))
        if opcion == "4":
            while True:
                print("[1] Desencriptar una clave")
                print("[2] Encriptar una clave")
                print("[3] Ver multiples ejemplos del hash")
                print("[4] Volver al menu")
                opcion2 = input("> ")
                if opcion2 == "1":
                    descifrar()
                if opcion2 == "2":
                    cifrar()
                if opcion2 == "3":
                    ejemplos()
                if opcion2 == '4':
                    print("Saliendo...\n")
                    break




            

        if opcion == '5':
            print("Saliendo...\n")
            break
input("\nPresiona ENTER para continuar...")
pruebas()


