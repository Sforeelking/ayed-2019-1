from sys import stdin
cont= 0
i= 0
j=0
def solve(l,x,n):
    global i
    global cont
    if i< l.index(x):
        suma= x+l[i]
        while suma<=n:
            if suma==n:
                cont+=1
                i+=1
                return solve(l,x,n)
            else:
                suma+= l[i]
        i+=1  
        return solve(l,x,n)
    else:
        solve2(l,x,n)
def solve2(l,x,n):
    global cont
    global j
    if j< l.index(x):
        summ= (2*x) + l[j]
        while summ <= n:
            if summ == n:
                cont+=1
                j+=1
                return solve2(l,x,n)
            else:
                summ+= x
        j+=1
        return solve2(l,x,n)
def main():
    n= int(stdin.readline().strip())
    l= [int(i) for i in stdin.readline().strip().split(",")]
    global cont
    global i
    global j
    for x in l:
        i= 0
        j=0
        if x==n:
            cont+=1
        else:
            ssum= 2*(x)
            while ssum<=n:
                if ssum==n:
                    cont+=1
                    solve(l,x,n)
                    break
                else:
                    ssum+=x
            solve(l,x,n)
    print(cont)
main()
    
    
