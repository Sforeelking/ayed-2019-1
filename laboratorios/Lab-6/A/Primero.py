from sys import stdin
def sort2(lista):
    izquierda, centro, derecha= [],[],[]
    if len(lista) > 1:
        pivote = len(lista[0])
        for i in lista:
            if len(i) < pivote:
                izquierda.append(i)
            elif len(i) == pivote:
                centro.append(i)
            elif len(i) > pivote:
                derecha.append(i)
        return sort2(izquierda)+centro+sort2(derecha)
    else:
      return lista
def solv(l,uno,k):
    for x in l:
        if l.count(x)==1:
            k.append([x])
        else:
            k.append(l[(l.index(x)):(l.index(x)+l.count(x))])
            for elem in l[(l.index(x)):(l.index(x)+l.count(x))-1]:
                l.remove(elem)
def main():
    casos= int(stdin.readline().strip())
    l=[]
    for elm in range(casos):
        m= int(stdin.readline().strip())
        l.append(m)
    l.sort()
    k,uno=[],[]
    solv(l,uno,k)
    k= sort2(k)
    for t in k:
        for u in t:
            print(u)

    
main()
