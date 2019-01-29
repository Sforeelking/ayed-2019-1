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
def busq(lista, busqueda):
    izquierda, derecha = 0, len(sort(lista)) - 1
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        elm = sort(lista)[mid]
        if elm == busqueda:
            return mid
        if busqueda < elm:
            derecha = mid - 1
        else:
            izquierda = mid + 1
    return -1
def main():
    busqueda= int(stdin.readline().strip())
    lista= stdin.readline().strip().split()
    print(busq(lista,busqueda))
main()
