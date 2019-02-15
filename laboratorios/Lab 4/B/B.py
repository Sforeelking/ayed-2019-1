from sys import stdin
def comp(l,y,cont):
    if cont < len(l):
        if len(l[cont])< len(l[cont-1]):
            y= len(l[cont-1])
        else:
            y= len(l[cont])
        return comp(l,y,cont+1)
    print(y)
def solv(l,x):
    for elem in l:
        if (x[0] in elem):
            elem.append(x[1])
            break
        elif (x[1] in elem):
            elem.append(x[0])
            break
        elif (l.index(elem)== len(l)-1)  and (x[0] not in elem) and (x[1] not in elem):
            l.append(x)
            break
    if len(l)==1:
        print(len(l[0]))
    else:
        comp(l,0,1)
def main():
    casos= int(stdin.readline().strip())
    l= []
    for i in range(casos):
        x= [int(j) for j in stdin.readline().strip().split()]
        if i==0:
            l.append(x)
            print(2)
        else:
            solv(l,x)
main()
    
