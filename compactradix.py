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


def counting_sort(arr, max_value, get_index):
    counts = [0] * max_value

  # Counting - O(n)
    for a in arr:s
        counts[get_index(a)] += 1
  
  # Accumulating - O(k)
    for i, c in enumerate(counts):
        if i == 0:
            continue
        else:
            counts[i] += counts[i-1]

  # Calculating start index - O(k)
    for i, c in enumerate(counts[:-1]):
        if i == 0:
            counts[i] = 0
            counts[i+1] = c

    ret = [None] * len(arr)
  # Sorting - O(n)
    for a in arr:
        index = counts[get_index(a)]
        ret[index] = a
        counts[get_index(a)] += 1
  
  return ret

def get_digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10

def get_num_difit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(arr, max_value):
    num_digits = get_num_difit(max_value)
    # O(k(n+k))
    for d in range(num_digits):
        # Counting sort takes O(n+k)
        arr = counting_sort(arr, max_value, lambda a: get_digit(a, d+1))
    return arr

arr=[9,22,222,2222]
x=radix_sort(arr,4)
print(x)
