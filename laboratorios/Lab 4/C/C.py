from sys import stdin
def mergeSort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       mergeSort(lefthalf)
       mergeSort(righthalf)
       i,j,k = 0,0,0
       while i < len(lefthalf) and j < len(righthalf):
           if (lefthalf[i]) < (righthalf[j]):
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]= righthalf[j]
           j=j+1
           k=k+1
   return(alist)
def main():
    n= (stdin.readline().strip().split())
    m= int(stdin.readline().strip())
    p=(mergeSort([int(i) for i in n]))
    for elm in range(1,len(mergeSort([int(i) for i in n]))+1):
        if sum(p[0:elm])>m:
            print(len(p[0:elm-1]))
            break
main()
