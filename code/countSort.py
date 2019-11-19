def countSort(arr):
    greatest = arr[0]
    retArr = [0]
    
    # find the biggets value
    for x in range (1,len(arr)):
        if arr[x] > greatest:
            greatest= arr[x]
        retArr.append(0)    
    index = [] 
    # creat an array form 0 to the biggest value
    for y in range (0,greatest+1):
        index.append(0)
    #adds 1 to the index of the of the index array and for each tiem the number shows up    
    for i in range(len(arr)):
        temps = arr[i] 
        index[temps] += 1
    
    # finds the biggest number for said index to show up at    
    for j in range (len(index)-1):
        index[j+1] += index[j] 
    
    
    # breaks cause 3 = 1 and 8 = 5
    for z in range (len(arr)):
        temp = arr[z]
        print(temp)

        retArr[index[temp]-1] = temp
        print(retArr)

        
        index[temp] -= 1
        
           
    return retArr
print (countSort([5,3,1,6,3,8,9,7,1]))        
