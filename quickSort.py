import math

def partition(sort_list, low, high):
    i = (low -1)
    print('low is=', low)
    print('high is=', high)
    pivot = sort_list[high]
    print('pivot=', pivot)
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            print('i= ', i,' j= ', j)
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
            print ('sortList at i= ', sort_list[i],' sortList at j= ',sort_list[j])
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    print('sort list in partition ',sort_list)
    return (i+1)
            
def quick_sort(sort_list,low,high):
    if low < high:
        pi = partition(sort_list, low, high)
        print (' iterator = ', pi)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)
        # print('sort list in quick sort',sort_list)
lst = []
# size = int(input("Enter size of the list: "))
#  for i in range(size):
#      elements = int(input("Enter an element"))
#      lst.append(elements)
List=[43532,55,645,4367,658,784,9769,6,54]
low = 0
high = len(List) - 1
print('unsorted list', List)
quick_sort(List, low, high)
print('sorted list',List)

# def quickSortCall(arr,)