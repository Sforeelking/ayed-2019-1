from sys import stdin
def solve(x,y,l,n):
    for elm in range(len(n)-1):
        l.append(abs(n[x]-n[y]))
        x,y= x+1,y+1
        if l[len(l)-1] in l[:len(l)-1]:
            break
    return l.sort()
def main():
    n= [int(i) for i in stdin.readline().strip().split()]
    x,y,l= 0,1,[]
    solve(x,y,l,n)
    if l == [int(h) for h in range(1,len(n))]:
        print(True)
    else:
        print(False)
main()
