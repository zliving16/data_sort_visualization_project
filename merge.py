import math

def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       print('left half is',lefthalf)
       print('righthalf is' , righthalf)

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
            #    print('alist at k= ',alist[k])
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
        #    print('for i is less than, alist at k= ',alist[k])
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
        #    print('for j is less than, alist at k= ',alist[k])
           j=j+1
        #    print('j= ', j)
           k=k+1
        #    print('k=',k)

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)