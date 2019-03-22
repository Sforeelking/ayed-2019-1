from sys import stdin
def main():
    m= [str(i) for i in stdin.readline().strip()]
    x,y=0, len(m)-1
    for elm in range(len(m)//2):
        m[x],m[y]=m[y],m[x]
        x,y= x+1,y-1
    print("".join(m))
main()
