import math

def flatten(List):
    print('list in flatten function= ',List)
    return [y for x in List for y in x]
 
def radix(List, idex=None, size=None):
    if List!=[]:
        print('list in radix is = ',List)
    # if 'b':
    #     print(b)
    # if bins:
    #     print(bins)
    if size == None:
        size = len(str(max(List)))
        # print('if s=none then s = len(str(max(List)))  size= ',size)
    if idex == None:
        idex = size
        # print('if p=none then idex = size')
 
    i = size - idex
    # print('i=s-p i= ', i)
 
    if i >= size:
        if List!=[]:
            print('i is greater than or equal to size list= ', List, ' and i= ',i, ' size= ',size)
        return List
 
    bins = [[] for _ in range(10)]
 
    for e in List:
        bins[int(str(e).zfill(size)[i])] += [e]
        # print('e=',e, ' bins[int(str(e).zfill(s)[i])]+[e] = ',bins[int(str(e).zfill(size)[i])])
        print('bins is= ',bins)
    return flatten([radix(b, idex-1, size) for b in bins])

a=[1, 15, 8, 7, 3, 33, 31]
b=radix(a, idex=None, size=None)
print(b)
