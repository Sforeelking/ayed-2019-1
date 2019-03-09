from sys import stdin
def solve(mayor,n,k):
    j=1
    if n in k:
        mayor.append(n)
    else:
        while j <= len(k):
            if sum(k[0:j])==n:
                for elm in k[0:j]:
                    mayor.append(elm)
                break
            elif sum(k[0:j])<n:
                j+=1
            else:
                k.remove(k[j-1])
        if j> len(k):
            for elm in k[0:j-1]:
                mayor.append(elm)
def solve2(menor,m,l):
    i=1
    if m in l:
        menor.append(m)
    else:
        while i <= len(l):
            if sum(l[0:i])==m:
                for elm in l[0:i]:
                    menor.append(elm)
                break
            elif sum(l[0:i])<n:
                i+=1
            else:
                for elm in l[0:i]:
                    menor.append(elm)
def solve3(mayor,menor):
    if len(menor)>len(mayor):
        for elem in mayor:
            if elem in menor:
                menor.remove(elem)
    else:
        for elem in menor:
            if elem in mayor:
                mayor.remove(elem)
    print(sum(menor)+sum(mayor))
def main():
    l=[int(i) for i in stdin.readline().strip().split(",")]
    n= int(stdin.readline().strip())
    m= int(stdin.readline().strip())
    l= l.sort()
    if n>m:
        solve([],n,l[::-1])
        solve2([],m,l)
        solve3(solve[0],solve2[0])
    else:
        solve1([],m,l)
        solve2([],n,l)
        solve3(solve[0],solve2[0])
main()
