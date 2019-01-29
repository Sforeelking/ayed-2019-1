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
def main():
    n= int(stdin.readline().strip())
    numbers= stdin.readline().strip().split()
    print(" ".join([str(i) for i in sort(numbers)]))
main()
