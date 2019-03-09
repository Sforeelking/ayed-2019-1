from sys import stdin
def solve(i,j,cont,l):
    while l:
        if ((j+1)>= len(l[i]) or l[i][j+1]==1):
            if ((i+1)>= len(l) or (l[i+1][j]==1)):
                break
            else:
                i+=1
                if (i == len(l)-1) and (j == len(l[0])-1):
                    cont,i,j= cont+1,0,0
                    solve2(0,l)
        else:
            j+=1
            if (i == len(l)-1) and (j == len(l[0])-1):
                    cont,i,j= cont+1,0,0
                    solve2(0,l)
    print(cont)
def solve2(g,l):
    if g< len(l):
        if 1 in l[g]:
            if (l[g].index(1))>1:
                l[g][l[g].index(1)-1]  = 1
            else:
                return solve2(g+1,l)
        else:
            l[g][len(l[g])-1]=1
def main():
    n,l= list(stdin.readline().strip().split(",")),[]
    for elm in n:
        k=[]
        for elem in elm:
            k.append(int(elem))
        l.append(k)
    solve(0,0,0,l)
main()
