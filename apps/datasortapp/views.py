from django.shortcuts import render,redirect
import math

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
            whatsHappening.append(f"if idex=size idex=  {idex}")
    
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
            whatsHappening.append(f"result at b is result= {result}  b= {b} idex= {idex} size=  {size} and bins=  {bins}")
    
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
    context={'sorttype': 'Gravity Sort', 'result':request.session['result'],
    'steps':request.session['steps'],'list':request.session['a']
    }

    return render(request,'datasortapp/merge.html',context)


