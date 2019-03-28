from sys import stdin
def solve(M,i,cont):
    if i< len(M)-1:
        y=0
        for elm in range(i,len(M)-1):
            if M[elm+1]> M[elm]  and y==0:
                x= M[elm+1] ^ M[elm]
                y=1
            elif M[elm+1]> M[elm]:
                x= x^ M[elm+1]
            elif M[elm+1]<= M[elm]:
                if y!=0:
                    if x> cont:
                        return solve(M,i+1,x)
                elif y==0:
                    if M[elm]> cont:
                        return solve(M,i+1,M[elm])
                break
    print(cont)
def main():
    N= int(stdin.readline().strip())
    M= [int(i) for i in stdin.readline().strip().split()]
    solve(M,0,0)
main()
