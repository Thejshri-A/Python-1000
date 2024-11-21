def sum_of_even_numbers_in_arr(arr):
    sum_even = 0
    
    for i in range(len(arr)):
        if arr[i]%2==0:
            sum_even += arr[i]
        else:
            continue
        
    return sum_even

arr= [1, 1, 3, 2, 4, 5, 6, 5, 15]
print(sum_of_even_numbers_in_arr(arr))