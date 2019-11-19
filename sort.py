import random
#Sorting Algorithms

#Selection (Better than bubble because because item switches are less, bubble sort switch more often)
def selection_sort(a_list):
    indexing_length = range(0, len(a_list)-1)

    for i in indexing_length:
        min_value = i

        for x in range(i+1, len(a_list)):
            if a_list[x] < a_list[min_value]:
                min_value = x
        
        if min_value != i:
            a_list[min_value], a_list[i] = a_list[i], a_list[min_value]
    return a_list

print(selection_sort([1,3,5,6,4,7,2]))

#Bubble 
def bubble_sort(a_list):
    for i in range(len(a_list)-1,0,-1):
        for x in range(i):
            if a_list[x] > a_list[x+1]:
                temp = a_list[x]
                a_list[x] = a_list[x+1]
                a_list[x+1] = temp
    return a_list
print(bubble_sort([2,5,7,4,3,1,6]))

#Cocktail Sort
def cocktail_sort(lst):
    if lst is None or len(lst) < 2:
        return lst
    length = len(lst)
    j = 0

    swap_occurred = True

    while swap_occurred:
        swap_occurred = False
        for i in range(length-1-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap_occurred = True
        
        if not swap_occurred:
            return lst
        
        swap_occurred = False

        for i in range(length - 1 - j, 0, -1):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                swap_occurred = True
        
        j += 1
            
lst = [6, 0, 9, 3, 7, 5, 4, 1, 8, 2]
print(cocktail_sort(lst))

#Bogo
import random
def reorder(a_list):
    n = len(a_list)
    for i in range(n):
        x = random.randint(0,n-1)
        a_list[i],a_list[x] = a_list[x],a_list[i]
    print(a_list)
    return a_list

def bogo_sort(a_list):
    count = 0
    while(True):
        for m in range(len(a_list)-1):
            if a_list[m] <= a_list[m+1]:
                pass
            else:
                break
        else:
            print(count)
            return a_list
        count +=1    
        a_list = reorder(a_list)
   
print(bogo_sort([2,3,2,10,13,7,9,82,4,25,98,351,73]))