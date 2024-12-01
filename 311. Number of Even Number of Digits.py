def num_of_even_num_of_digits(arr):
    return sum(1 for num in arr if len(str(abs(num)))%2==0)

arr=[12, 134, 1456, 234232, 14, 5]
print(num_of_even_num_of_digits(arr))