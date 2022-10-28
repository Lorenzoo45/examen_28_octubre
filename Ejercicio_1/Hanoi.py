def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

# moverTorre(3,"A","B","C")# Ejemplo sencillo con solo tres agujas
moverTorre(64,"A","B","C")# Ejemplo sencillo con solo tres agujas

#El número de movimientos necesarios para mover correctamente una torre de 64 discos es 264−1