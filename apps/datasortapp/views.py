from django.shortcuts import render,redirect
import math
import random

def inputdata(request):
    request.session.clear()
    return render(request,'datasortapp/datainput.html')
def radixprocess(request):
    # request.session['a']=request.POST['dataArray']
    # data=request.session['a']
    # request.session['a']=[int(s) for s in data.split(',')]

    return redirect('/radix')

def radixpage(request):
    if 'a' not in request.session:
        return redirect('/')
    whatsHappening=[]
    def flatten(some_list):
        """
        Flatten a list of lists.
        Usage: flatten([[list a], [list b], ...])
        Output: [elements of list a, elements of list b]
        """
        new_list = []
        
        for sub_list in some_list:
            new_list += sub_list
            whatsHappening.append(f"for sublist in some list  {some_list}  at sub list=  {sub_list}  and new list=  {new_list}")
        return new_list
    
    def radix(some_list, idex=None, size=None):
        """
        Recursive radix sort
        Usage: radix([unsorted list])
        Output: [sorted list]
        """
        if size == None:
            largest_num = max(some_list)
            largest_num_str = str(largest_num)
            largest_num_len = len(largest_num_str)
            size = largest_num_len
    
        if idex == None:
            idex = size
            # whatsHappening.append(f"if idex=size idex=  {idex}")
    
        i = size - idex 
    
        if i >= size:
            return some_list
    
        bins = [[] for _ in range(10)]
    
        for e in some_list:
            num_s  = str(e).zfill(size)
            dest_c = num_s[i]
            dest_i = int(dest_c) 
            bins[dest_i] += [e]
            whatsHappening.append(f"bins at e= {bins[dest_i]}")
            whatsHappening.append(f"bins=  {bins} at e=  {e}")

        whatsHappening.append(f"bins= {bins}")
    
        result = []
        for b in bins:
            if b == []:
                continue
            result.append(radix(b, idex-1, size))
            whatsHappening.append(f"result at b is result= {result} and bins=  {bins}")
    
        flattened_result = flatten(result)
    
        return flattened_result

    a=request.session['a']
    # a=[1, 151, 28 , 8, 333, 33, 3]
    x=radix(a, idex=None, size=None)
    context={'steps':whatsHappening,'result':x,'list':a,'sorttype':'Radix'}
    return render(request,'datasortapp/merge.html',context)

def quickSortProcess(request):
    # request.session['a']=request.POST['dataArray']
    # data=request.session['a']
    # request.session['a']=[int(s) for s in data.split(',')]

    return redirect('/quicksort')

def quickSort(request):
    if 'a' not in request.session:
        return redirect('/')
    whatsHappening=[]
    other=[]
    def partition(sort_list, low, high):
        i = (low -1)
        pivot = sort_list[high]
        for j in range(low, high):
            if sort_list[j] <= pivot:
                i += 1
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
                whatsHappening.append(f'{sort_list}')
        sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
        whatsHappening.append(f'{sort_list}')
        return (i+1)
    def quick_sort(sort_list,low,high):
        if low < high:
            pi = partition(sort_list, low, high)
            # whatsHappening.append(f'z {sort_list}')
            return  quick_sort(sort_list, low, pi-1), quick_sort(sort_list, pi+1, high)
           
    List=request.session['a']
    other.append(f'{List}')
    low = 0
    high = len(List) - 1
    whatsHappening.append(f"unsorted list {request.session['a']}")
    quick_sort(List, low, high)
    whatsHappening.append(f"sorted list is {List}")
    context={'steps':whatsHappening,'result':List,'list':other, 'sorttype':'Quick Sort'}
    return render(request,'datasortapp/merge.html',context)

def mergeprocess(request):
    return redirect('/merge')

def merge(request):
    if 'a' not in request.session:
        return redirect('/')
    whatsHappening=[]
    def mergeSort(alist):

        whatsHappening.append(f'Splitting {alist}')

        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            whatsHappening.append(f'left half is {lefthalf}')
            whatsHappening.append(f'righthalf is  {righthalf}')

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

        whatsHappening.append(f"Merging {alist}")
        return alist
    temp=str(request.session['a'])
    alist = request.session['a']
    # List=request.session['a']
    result=mergeSort(alist)
    whatsHappening.append(f'{alist}')
    context={'steps':whatsHappening,'list':temp,'result':result,'sorttype':'Merge'}
    return render(request, 'datasortapp/merge.html', context)

def gravityProcess(request):
    whatsHappening=[]
    def beadsort(input_list):
        return_list = []
        transposed_list = [0] * max(input_list)
        whatsHappening.append(f'Unsorted list is{input_list}')
        for num in input_list:
            transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
            whatsHappening.append(f'Number= {num}' )
            # and Transposed list at num {transposed_list[:num]} 

        for _ in input_list:
            return_list.append(sum(n > 0 for n in transposed_list))
            whatsHappening.append(f'{return_list}')
            transposed_list = [n - 1 for n in transposed_list]

        whatsHappening.append(return_list)
        # whatsHappening.append(f'inputlist={input_list} ')
        return return_list[::-1]
    request.session['result']=beadsort(request.session['a'])  
    request.session['steps']=whatsHappening
    return redirect('/gravitySort')


def gravitySort(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Gravity Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def countProcess(request):
    whatsHappening=[]
    def countSort(arr):
        greatest = arr[0]
        retArr = [0]
        
        for x in range (1,len(arr)):
            if arr[x] > greatest:
                greatest= arr[x]
            retArr.append(0)    
        index = [] 
        for y in range (0,greatest+1):
            index.append(0)

        for i in range(len(arr)):
            temps = arr[i] 
            index[temps] += 1

        for j in range (len(index)-1):
            index[j+1] += index[j] 
        
        
        for z in range (len(arr)):
            temp = arr[z]
            whatsHappening.append(f'{retArr}')
            retArr[index[temp]-1] = temp
            index[temp] -= 1
     
            
            
        return retArr
    request.session['result']=countSort(request.session['a'])  
    request.session['steps']=whatsHappening
    return redirect('/countSort')

def countpage(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Count Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def heapProcess(request):
    whatsHappening=[]
    def heapify(arr, n, i): 
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2 
            
        if l < n and arr[i] < arr[l]: 
            largest = l 
        
        if r < n and arr[largest] < arr[r]: 
            largest = r 
        
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i]              
            return heapify(arr, n, largest) 
  
 
    def heapSort(arr): 
        n = len(arr) 
        whatsHappening.append(f'{arr}') 
        for i in range(n, -1, -1):             
            heapify(arr, n, i)     
        
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]  
            # whatsHappening.append(f'f {arr}')
            heapify(arr, i, 0) 
            whatsHappening.append(f'{arr}')

        return arr
    temp=str(request.session['a'])
    data=request.session['a']       
    request.session['result']=heapSort(data)  
    request.session['steps']=whatsHappening 
    request.session['a']=temp
    return redirect('/heapSort')




def heapPage(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Heap Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def bogoProcess(request):
    whatsHappening=[]
    def reorder(a_list):
        n = len(a_list)
        for i in range(n):
            x = random.randint(0,n-1)
            a_list[i],a_list[x] = a_list[x],a_list[i]
        # temp=a_list
        whatsHappening.append(f'{a_list}')
        return a_list

    def bogo_sort(a_list):
        count = 0
        while(True):
            for m in range(len(a_list)-1):
                if a_list[m] <= a_list[m+1]: 
                    pass
                else:
                    break
                    # whatsHappening.append(a_list)
            else:
                whatsHappening.append(f'Bogo ran {count} times to sort it')
                return a_list  
            count +=1
            # temp=a_list
            # whatsHappening.append(temp)
            a_list= reorder(a_list)
            # return a_list

    temp=str(request.session['a'])
    data=request.session['a']
    request.session['result']=bogo_sort(data)  
    request.session['steps']=whatsHappening
    request.session['a']=temp 
    return redirect('/bogo')

def bogoPage(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Bogo Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def selectionProcess(request):
    whatsHappening=[]
    def selection_sort(a_list):
        indexing_length = range(0, len(a_list)-1)

        for i in indexing_length:
            min_value = i

            for x in range(i+1, len(a_list)):
                if a_list[x] < a_list[min_value]:
                    min_value = x
            whatsHappening.append(f'{a_list}')
            
            if min_value != i:
                a_list[min_value], a_list[i] = a_list[i], a_list[min_value]
        return a_list
    temp=str(request.session['a'])
    data=request.session['a']
    request.session['result']=selection_sort(data)  
    request.session['steps']=whatsHappening 
    request.session['a']=temp
    return redirect('/selection')

def selectionPage(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Selection Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def routeProcess(request):
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]
    x=request.POST['sortType']
    return redirect(f'/{x}/process')

def cocktailProcess(request):
    whatsHappening=[]
    def cocktail_sort(lst):
        if lst is None or len(lst) < 2:
            return lst
        length = len(lst)
        j = 0
        whatsHappening.append(f'{lst}')

        swap_occurred = True

        while swap_occurred:
            swap_occurred = False
            for i in range(length-1-j):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    whatsHappening.append(f'{lst}')
                    swap_occurred = True
            
            if not swap_occurred:
                return lst
            
            swap_occurred = False

            for i in range(length - 1 - j, 0, -1):
                if lst[i] < lst[i-1]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                    whatsHappening.append(f'{lst}')
                    swap_occurred = True
            
            j += 1
    temp=str(request.session['a'])            
    lst =request.session['a']
    whatsHappening.append(f'{lst}')
    request.session['result']=cocktail_sort(request.session['a'])  
    request.session['steps']=whatsHappening 
    request.session['a']=temp



    return redirect('/cocktail')

def cocktailPage(request):
    if 'a' not in request.session:
        return redirect('/')
    
    context={'sorttype': 'Cocktail Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

def bubbleProcess(request):
    whatsHappening=[]
    def bubble_sort(a_list):
        for i in range(len(a_list)-1,0,-1):
            # whatsHappening.append(f'a {a_list}')
            for x in range(i):
                whatsHappening.append(f'{a_list}')
                if a_list[x] > a_list[x+1]:
                    temp = a_list[x]
                    a_list[x] = a_list[x+1]
                    a_list[x+1] = temp
                    whatsHappening.append(f'{a_list}')
        return a_list
    temp=str(request.session['a'])
    lst =request.session['a']
    whatsHappening.append(f'{lst}')
    request.session['result']=bubble_sort(request.session['a'])  
    request.session['steps']=whatsHappening 
    request.session['a']=temp


    return redirect('/bubble')

def bubblePage(request):
    if 'a' not in request.session:
        return redirect('/')
    
    context={'sorttype': 'Bubble Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)

import numpy as np
from PIL import Image
from skimage import color
from scipy.misc import imsave

import numpy as np
def colortest(request):

    # newImage = np.random.randint(0, 255, (300, 300, 3))

    # in_hsv_h = color.convert_colorspace(newImage, 'RGB', 'HSV')
    # in_hsv_s = in_hsv_h.copy()
    # in_hsv_v = in_hsv_h.copy()

    # for i in range(newImage.shape[0]):
    #     in_hsv_h[i,:,0] = np.sort(in_hsv_h[i,:,0])
    #     in_hsv_s[i,:,1] = np.sort(in_hsv_s[i,:,1])
    #     in_hsv_v[i,:,2] = np.sort(in_hsv_v[i,:,2])
    # imsave('testing-sorted-hue.png', color.convert_colorspace(in_hsv_h, 'HSV', 'RGB'))
    # imsave('testing-sorted-saturation.png', color.convert_colorspace(in_hsv_s, 'HSV', 'RGB'))
    # imsave('testing-sorted-value.png', color.convert_colorspace(in_hsv_v, 'HSV', 'RGB'))

    # img = np.zeros((300, 300, 3), dtype='float32') # hsv works in range from 0 - 1

    # for i in range(img.shape[1]):
    #     img[:,i,:] = i / img.shape[1], 1.0, 1.0

    # in_rgb = color.convert_colorspace(img, 'HSV', 'RGB')
    # imsave('initial_hsv_1.png', in_rgb)

    # for i in range(img.shape[0]):
    #     np.random.shuffle(img[i,:,:])

    # imsave('initial_hsv_1_shuffled.png', color.convert_colorspace(img, 'HSV', 'RGB'))
    # def bubblequest(A):
    #     swaps = []
    #     for i in range(len(A)):
    #         for k in range(len(A) - 1, i, -1):
    #             if (A[k] < A[k - 1]):
    #                 swaps.append([k, k - 1])
    #                 tmp = A[k]
    #                 A[k] = A[k - 1]
    #                 A[k - 1] = tmp
    #     return A, swaps
    # currentMove=0
    # maxMoves=200
    # moves=[]
    # def swap_pixels(row, places):
    #     tmp = img[row,places[0],:].copy()
    #     img[row,places[0],:] = img[row,places[1],:]
    #     img[row,places[1],:] = tmp


    
    # movie_image_step = maxMoves // 120
    # movie_image_frame = 0

    # while currentMove < maxMoves:
    #     for i in range(img.shape[0]):
    #         if currentMove < len(moves[i]) - 1:
    #             swap_pixels(i, moves[i][currentMove])

    #     if currentMove % movie_image_step == 0:
    #         imsave('%s/%05d.png' % (args.sorter, movie_image_frame), color.convert_colorspace(img, 'HSV', 'RGB'))
    #         movie_image_frame += 1
    #     currentMove += 1

    return render(request, 'datasortapp/test.html')



