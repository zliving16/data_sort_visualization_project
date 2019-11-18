import math

def flatten(some_list):
    """
    Flatten a list of lists.
    Usage: flatten([[list a], [list b], ...])
    Output: [elements of list a, elements of list b]
    """
    new_list = []
    for sub_list in some_list:
        new_list += sub_list
        print('for sublist in some list ' , some_list ,' at sub list= ', sub_list,' and new list= ',new_list)
    return new_list
 
def radix(some_list, idex=None, size=None):
    """
    Recursive radix sort
    Usage: radix([unsorted list])
    Output: [sorted list]
    """
    # Initialize variables not set in the initial call
    if size == None:
        largest_num = max(some_list)
        print('if size is equal to none largest num= ', largest_num)
        largest_num_str = str(largest_num)
        print('if size is equal to none largest num str= ', largest_num_str)
        largest_num_len = len(largest_num_str)
        print('if size is equal to none largest larges num len= ', largest_num_len)
        size = largest_num_len
        print('if size is equal to none largest size= ', size)
 
    if idex == None:
        idex = size
        print('if idext is equalt to none idex=size idex= ', idex)
 
    # Translate the index we're looking at into an array index.
    # e.g., looking at the 10's place for 100:
    # size: 3
    # idex: 2
    #    i: (3-2) == 1
    # str(123)[i] -> 2
    i = size - idex 
 
    # The recursive base case.
    # Hint: out of range indexing errors
    if i >= size:
        print('some list at if i is greater than or equal to size', some_list, 'i= ',i, 'size= ',size)
        return some_list
 
    # Initialize the bins we will place numbers into
    bins = [[] for _ in range(10)]
 
    # Iterate over the list of numbers we are given
    for e in some_list:
        # The destination bin; e.g.,:
        #   size: 5
        #      e: 29
        #  num_s: '00029'
        #      i: 3
        # dest_c: '2'
        # dest_i: 2
        num_s  = str(e).zfill(size)
        print('num s is equal to str(e).zfill(size) num_s= ', num_s)
        dest_c = num_s[i]
        print('dest c =nums at s of i dest_c= ',dest_c)
        dest_i = int(dest_c) 
        print('dest i is equal to int dest c  dest i= ',dest_i)
        bins[dest_i] += [e]
        print('bins at dest i+[e]= ',bins[dest_i])
        # print('for e in some list ', some_list,' at e= ', e)
        print ('e= ', e , 'in some list')
 
    result = []
    for b in bins:
        #If the bin is empty it skips the recursive call
        if b == []:
            continue
        # Make the recursive call
        # Sort each of the sub-lists in our bins
        result.append(radix(b, idex-1, size))
        # print('for b in bins ', some_list,' at b= ',b)
        print('result at b is result= ',result,'b is equal to b=',b,' idex= ',idex,' size= ', size )
 
    # Flatten our list
    # This is also called in our recursive call,
    # so we don't need flatten to be recursive.
    flattened_result = flatten(result)
 
    return flattened_result

# a=[346546,564664,376,7587,6985,9870,7865,7,4565,46,4576,58,796,8,97,6,89,678,56,745,764,754,79,68,97,97,80,90,87,976,865,745,645,6653,387,7,876,85,768,566,45,654,3,4,765,754,88,78,76,876,876,876,876,8]
a=[1, 15, 8, 7, 3, 31]
print(radix(a, idex=None, size=None))
 