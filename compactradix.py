import math

def flatten(List):
    print('list in flatten function= ',List)
    return [y for x in List for y in x]
 
def radix(List, idex=None, size=None):
    if List!=[]:
        print('list in radix is = ',List)
    if size == None:
        size = len(str(max(List)))
    if idex == None:
        idex = size
 
    i = size - idex
 
    if i >= size:
        if List!=[]:
            return List
 
    bins = [[] for _ in range(10)]

    for e in List:
        bins[int(str(e).zfill(size)[i])] += [e]
        print('bins is= ',bins)
    return flatten([radix(b, idex-1, size) for b in bins])

a=[1, 15, 8, 7, 3, 33, 31]
b=radix(a, idex=None, size=None)
print(b)
