from sys import stdin
import math
def sis(n,k,suma,b):
    if k<=n:
        suma= suma+ (fact(n,k)*b[k])
        return sis(n,k+1,suma,b)
    b.append(suma)
def fact(n,k):
    return int((math.factorial(n))/((math.factorial(k))*(math.factorial(n-k))))
def main():
    b=[1]
    n= int(stdin.readline().strip())
    for elm in range(1,n+1):
        sis(elm-1,0,0,b)
    print(b[len(b)-1])
main()
