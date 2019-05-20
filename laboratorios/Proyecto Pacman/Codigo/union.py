from sys import stdin
import  time
from random import shuffle, randint     
from itertools import product

def main():
    a = True
    print("Bienvenido")
    while a:
        print("-----Menu------")
        print("Seleccione La Opcion Deseada")
        print("1. Generar Matriz")
        print("2. Empezar Juego")
        print("3. Salir")
        respuesta = int(input())
        if respuesta == 1 :
            print("Ingrese la dimencion del laberinto Ejemplo(Z Z)")
            x = int(input())
            y = int(input())
            Lab = laberinto(10,10)
            matriz = OrganizaMat(Lab,x,y)
            for i in matriz:
                print(*i)
        print("_------------------")
        if respuesta == 2 :        
            movimiento(1,1,matriz)
        if respuesta == 3 :
            break

    
def movimiento(x,y,matriz):
    if matriz [x][y] == "3":
        return True
    elif matriz [x][y] == "1":
        print("hay pared en ",x,y)
        return False
    elif matriz [x][y]=="x":
        print("se ha visitado",x,y)
        return False
    #marcas las comidas
    matriz [x][y]= "x"
    for i in matriz :
        print(*i)
    print("________________________________")
    time.sleep(2)

    if ((x < len(matriz)-1 and movimiento(x+1, y,matriz))or (y > 0 and movimiento(x, y-1,matriz))
        or (x > 0 and movimiento(x-1, y,matriz))or (y < len(matriz)-1 and movimiento(x, y+1,matriz))):
        return True
    return False    
    
    



def OrganizaMat(Lab,x,y):
    a = 0
    b = x*4+2
    cont = 0
    matriz = []
    for i in range (x*2+2):
        linea = Lab[a:b]
        linea = linea.strip()
        linea2 = linea.split(' ')
        matriz.append(linea2)
        cont+=1
        if cont >= 2:
            cont = 0
            a+= 2
            b+= 2
        a+= x*4+2
        b+= x*4+2

    return (matriz)








def laberinto(m, n):
    def vecinos(i, j):                  
        if 0 < i: yield i - 1, j
        if i < m - 1: yield i + 1, j
        if 0 < j: yield i, j - 1
        if j < n - 1: yield i, j + 1

    def visitar(i, j):                  
        X.add((i, j))                   
        N = list(vecinos(i, j)); shuffle(N)  
        for h, k in N:                  
            if (h, k) in X: continue    
            A[i + h + 1][j + k + 1] = '0 '  
            visitar(h, k)               

    A = [['1 ']*(2*n + 1) for i in range(2*m + 1)]  
    for i, j in product(range(1, 2*m + 1, 2), range(1, 2*n + 1, 2)):
        A[i][j] = '0 '                   
    X = set()                           
    visitar(randint(0, m - 1), randint(0, n - 1))  
    return('\n'.join(''.join(fila) for fila in A))  


main()
