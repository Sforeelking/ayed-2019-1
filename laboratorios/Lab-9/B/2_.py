from sys import stdin
def solve(l):
    if len(l)%2 !=0:
        print((l[len(l)//2])/1)
    else:
        print((l[len(l)//2] + l[(len(l)//2)-1])/2)
def main():
    n,l= int(stdin.readline().strip()), []
    for elm in range(n):
        m= int(stdin.readline().strip())
        l.append(m)
        l.sort()
        solve(l)
main()
