from sys import stdin
def solve(n,m):
    l=[]
    for elm in range(0,len(n)):
        l.append(n[elm-m])
    return l
def main():
    n,m= [int(i) for i in stdin.readline().strip().split()], int(stdin.readline().strip())
    print(solve(n,m))
main()
