#Supongo que la matriz es de 3x3
#Calcula el determinante de una matriz de 3x3 por el metodo de Sarrus recursivo
def SarrusR(matriz):
    det = 0
    for i in range(len(matriz)):
        det += (-1) ** i * matriz[0][i] * SarrusR([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
    return det

matriz = [[6,2,2],[7,5,3],[7,7,1]]
print(len(matriz))
print(SarrusR(matriz))
# no sé por qué no funciona pero no funciona el Iterativo SI






def SarrusI():
    
        # Inicializamos la matriz
        matriz = [[0,0,0],[0,0,0],[0,0,0]]
    
        # Pedimos los valores de la matriz
        for i in range(3):
            for j in range(3):
                matriz[i][j] = int(input("Introduce el valor de la posición " + str(i) + "," + str(j) + ": "))
        print(matriz)
        # Calculamos el determinante
        det = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][1] * matriz[1][0] * matriz[2][2] - matriz[0][0] * matriz[1][2] * matriz[2][1]
    
        # Mostramos el resultado
        print("El determinante de la matriz es: " + str(det))