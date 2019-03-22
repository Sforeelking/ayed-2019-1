from sys import stdin
def main():
    n=[int(i) for i in stdin.readline().strip().split("→")]
    for elm in n:
        if n.count(elm)>1:
            n.remove(elm)
            n= "→".join([str(j) for j in n])
            print(n)
            print(True)
            break
main()
