#Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
# restar;
# dividir;
# eliminar un término;
# determinar si un término existe en un polinomio.
class Nodo(object):
    info,sig = None,None
class datoPolinomio(object):
    """Clase del dato del polinomio"""
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino
class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux = aux.sig
    if aux is not None and aux.info.termino == termino:
        return aux.info.valor
    else:
        return 0
        
def agregar_termino(polinomio,termino,valor):
    aux = Nodo()
    dato = datoPolinomio(valor,termino)
    aux.info = dato
    if(termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while actual.sig is not None and actual.sig.info.termino > termino:
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux

def restar(polinomio1,polinomio2):
    polinomio3 = Polinomio()
    for i in range(polinomio1.grado + 1):
        valor = obtener_valor(polinomio1,i) - obtener_valor(polinomio2,i)
        if valor != 0:
            agregar_termino(polinomio3,i,valor)
    return polinomio3

def dividir(polinomio1,polinomio2):
    polinomio3 = Polinomio()
    polinomio4 = Polinomio()
    for i in range(polinomio1.grado + 1):
        valor = obtener_valor(polinomio1,i) / obtener_valor(polinomio2,i)
        if valor != 0:
            agregar_termino(polinomio3,i,valor)
    return polinomio3

def eliminar_termino(polinomio,termino):
    aux = polinomio.termino_mayor
    if aux is not None and aux.info.termino == termino:
        polinomio.termino_mayor = aux.sig
        aux.sig = None
    else:
        while aux.sig is not None and aux.sig.info.termino > termino:
            aux = aux.sig
        if aux.sig is not None and aux.sig.info.termino == termino:
            aux.sig = aux.sig.sig
def existe_termino(polinomio,termino):
    aux = polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux = aux.sig
    if aux is not None and aux.info.termino == termino:
        return True
    else:
        return False

