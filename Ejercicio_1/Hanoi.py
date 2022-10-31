def moverTorre(altura,origen, destino, intermedio):
    if altura >= 20:
        try:
            raise ValueError("La altura no puede ser mayor o igual a 20 discos ya que sino los calculos son inabordables")
        except ValueError as e:
            print(e)
            nueva_altura = input("Prueba con un nuevo valor:")
            moverTorre(int(nueva_altura),origen, destino, intermedio)
    if altura >= 1 and altura<20:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)


# moverTorre(3,"A","B","C")# Ejemplo sencillo con solo tres agujas
# moverTorre(64,"A","B","C")# Ejemplo sencillo con solo tres agujas

#El número de movimientos necesarios para mover correctamente una torre de 64 discos es 264−1

#tengo que poner las condiciones para que no pete el programa