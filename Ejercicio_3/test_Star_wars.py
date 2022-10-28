import pytest
import sys
sys.path.insert(0,"Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/examen_28_octubre/Ejercicio_3")
from Star_Wars import Nave,orden_nombres
#nos creamos todas las naves que vamos a usar
nave_1 = Nave("Halcón Milenario", 34.37, 4, 6)
nave_2 = Nave("Estrella de la Muerte", 120000, 342953, 843342)
nave_3 = Nave("AT-AT", 20, 5, 40)
nave_4 = Nave("AT-ST", 2, 2, 0)
nave_5 = Nave("AT-TE", 5, 2, 0)
nave_6 = Nave("AT-PT", 3, 2, 0)
nave_7 = Nave("AT-AT Walker", 20, 5, 40)
def test_orden_nombres():
    lista = [nave_1, nave_2, nave_3, nave_4, nave_5, nave_6, nave_7]
    lista_ordenada = orden_nombres(lista)
    assert lista_ordenada[0] == nave_3
    assert lista_ordenada[1] == nave_7
    assert lista_ordenada[2] == nave_6
    assert lista_ordenada[3] == nave_4
    assert lista_ordenada[4] == nave_5
    assert lista_ordenada[5] == nave_2
    assert lista_ordenada[6] == nave_1
listaNaves = [nave_1,nave_2,nave_3,nave_4,nave_5,nave_6,nave_7]
naves_ordenadas = orden_nombres(listaNaves)
for nave in naves_ordenadas:
    print(nave)
# for nave in cinco_mayores(listaNaves):
#     print(nave)