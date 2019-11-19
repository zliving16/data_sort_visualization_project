def beadsort(input_list):
    return_list = []
    transposed_list = [0] * max(input_list)

    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
        

    for _ in input_list:
        return_list.append(sum(n > 0 for n in transposed_list))
        print (return_list)
        transposed_list = [n - 1 for n in transposed_list]


    return return_list[::-1]   
print(beadsort([5,4,2,1,3,6,7,8,9]) )   