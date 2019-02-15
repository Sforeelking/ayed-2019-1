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
    n= stdin.readline().strip().split()
    m= [int(i) for i in n]
    cont=0
    for elm in range(0,len(n)):
        if int(n[elm])!= mergeSort(m)[elm]:
            cont+=1
    print((cont//2)+1 )
main()
    
