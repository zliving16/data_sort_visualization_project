from django.shortcuts import render,redirect
import math
import random

def inputdata(request):
    return render(request,'datasortapp/datainput.html')
def radixprocess(request):
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]

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
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]

    return redirect('/quicksort')

def quickSort(request):
    if 'a' not in request.session:
        return redirect('/')
    whatsHappening=[]
    def partition(sort_list, low, high):
        i = (low -1)
        whatsHappening.append(f'low is= {low}')
        whatsHappening.append(f'high is= {high}')
        pivot = sort_list[high]
        whatsHappening.append(f'pivot= {pivot}')
        for j in range(low, high):
            if sort_list[j] <= pivot:
                i += 1
                whatsHappening.append(f"i= {i}  j= {j}")
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
                whatsHappening.append(f"sort List at i=  {sort_list[i]}  sort List at j= {sort_list[j]}")
        sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
        whatsHappening.append(f'sort list in partition is {sort_list}')
        return (i+1)
    def quick_sort(sort_list,low,high):
        if low < high:
            pi = partition(sort_list, low, high)
            whatsHappening.append(f' iterator =  {pi}')
            return  quick_sort(sort_list, low, pi-1), quick_sort(sort_list, pi+1, high)
           

    List=request.session['a']
    low = 0
    high = len(List) - 1
    whatsHappening.append(f"unsorted list {List}")
    x=quick_sort(List, low, high)
    whatsHappening.append(f"sorted list is {List}")
    context={'steps':whatsHappening,'result':x,'list':List, 'sorttype':'Quick Sort'}
    return render(request,'datasortapp/merge.html',context)

def mergeprocess(request):
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]
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

    alist = request.session['a']
    result=mergeSort(alist)
    whatsHappening.append(f'{alist}')
    context={'steps':whatsHappening,'list':alist,'result':result,'sorttype':'Merge'}
    return render(request, 'datasortapp/merge.html', context)

def gravityProcess(request):
    whatsHappening=[]
    def beadsort(input_list):
        return_list = []
        transposed_list = [0] * max(input_list)

        for num in input_list:
            transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
            whatsHappening.append(f'Number= {num}  and Transposed list at num {transposed_list[:num]} ' )

        for _ in input_list:
            return_list.append(sum(n > 0 for n in transposed_list))
            # whatsHappening.append(return_list)
            transposed_list = [n - 1 for n in transposed_list]
            # whatsHappening.append(f'transposed list{transposed_list}')

        # whatsHappening.append(f'inputlist={input_list} ')
        return return_list[::-1]
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]
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
            whatsHappening.append(f' Return Array={retArr}')
            retArr[index[temp]-1] = temp
            index[temp] -= 1
     
            
            
        return retArr
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    request.session['a']=[int(s) for s in data.split(',')]
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
        # whatsHappening.append(f'largest= {largest}')   
    
        
        if l < n and arr[i] < arr[l]: 
            largest = l 
            # whatsHappening.append(f'largest= {largest}')   

    
        
        if r < n and arr[largest] < arr[r]: 
            largest = r 
            # whatsHappening.append(f'largest= {largest}')   

        
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i]  
            # whatsHappening.append(f'arr[i]= {arr[i]} arr[largest]={arr[largest]}')   

    
            
            return heapify(arr, n, largest) 
  
 
    def heapSort(arr): 
        n = len(arr) 
        print(arr)
        
        for i in range(n, -1, -1): 
            
            heapify(arr, n, i) 
            
    
        
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]  
            heapify(arr, i, 0) 
            whatsHappening.append(f'{arr}')
            # i={i} arr[i]={arr[i]} array=

        return arr
            
  
 
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    data=[int(s) for s in data.split(',')]
    request.session['result']=heapSort(data)  
    request.session['steps']=whatsHappening 
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
        # whatsHappening.append(a_list)
        return a_list

    def bogo_sort(a_list):
        count = 0
        while(True):
            for m in range(len(a_list)-1):
                if a_list[m] <= a_list[m+1]:
                    whatsHappening.append(a_list)
                    pass
                else:
                    whatsHappening.append(a_list)
                    break
            else:
                whatsHappening.append(count)
                return a_list
            count +=1    
            a_list = reorder(a_list)
    request.session['a']=request.POST['dataArray']
    data=request.session['a']
    data=[int(s) for s in data.split(',')]
    request.session['result']=bogo_sort(data)  
    request.session['steps']=whatsHappening 
    return redirect('/bogo')

def bogoPage(request):
    if 'a' not in request.session:
        return redirect('/')
    context={'sorttype': 'Heap Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)




