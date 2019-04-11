from sys import stdin
def solve(cont,x,y,n,N):
    if y<= len(N)-1:
        if N[x]<n or N[y]<n:
            N[x]= (1*N[x] + 2*N[y])
            N.remove(N[y])
            N.sort()
            return solve(cont+1,x,y,n,N)
        else:
            return solve(cont,x+1,y+1,n,N)
    else:
        try:
            for elm in range(len(N)):
                if N[elm]< n:
                    return solve(cont,0,1,n,N)
                elif N[elm]>= n and elm==len(N)-1:
                    print(cont)
        except RecursionError:
            print("-1")
def main():
    m,n =[int(i) for i in stdin.readline().strip().split(" ")]
    N= [int(i) for i in stdin.readline().strip().split(" ")]
    N.sort()
    solve(0,0,1,n,N)
main()
