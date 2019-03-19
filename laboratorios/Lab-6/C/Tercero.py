from sys import stdin
import math
def solve(k,n,p,q):
    for elm in range(k,n):
        p[elm]= p[elm-2]+ 2* q[elm-1]
        q[elm]= p[elm-1]+ q[elm-2]
    return p[n-1]
def main():
    n= int(stdin.readline().strip())
    p,q= [0]* (n+1), [0]* (n+1)
    p[0],p[1],q[0],q[1]= 1,0,0,1
    print(solve(2,n+1,p,q))
main()

    
    
