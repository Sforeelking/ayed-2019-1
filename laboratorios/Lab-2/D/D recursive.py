from sys import stdin
def sort(lista):
    izquierda,centro,derecha = [],[],[]
    if len(lista) > 1:
        pivote = int(lista[0])
        for i in lista:
            if int(i) < pivote:
                izquierda.append(int(i))
            elif int(i) == pivote:
                centro.append(int(i))
            elif int(i) > pivote:
                derecha.append(int(i))
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista
def solv(lista,n):
    print(lista,n)
    if len(lista)>= ((n//2) +1):
        if lista.count(lista[0])> n/2:
            return True
        else:
            return solv(lista[lista.count(lista[0]): ],n)
    else:
        return False
def main():
    n= int(stdin.readline().strip())
    lista= stdin.readline().strip().split()
    print(solv(sort(lista),n))
main()
