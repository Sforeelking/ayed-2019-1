from sys import stdin
def solve(a):
    suma2=0
    for x in range(len(a)):
        suma=0
        for elm in range(x):
            suma= suma+ a[elm][0]
        suma2+= (suma+ (a[x][0]- a[x][1]))
    print(int(suma2/len(a)))
def main():
    casos,n= int(stdin.readline().strip()),[]
    for elm in range(casos):
        N= [int(i) for i in stdin.readline().strip().split()]
        n.append(N[::-1])
    n.sort()
    solve(n)
main()
    
    
