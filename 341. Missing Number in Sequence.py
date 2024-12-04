def missing_number_in_seq(arr):
    n=len(arr)
    expected_sum = (n*(n+1))//2
    actual_sum = sum(arr)
    return expected_sum-actual_sum

arr=[1, 0, 3]
print(missing_number_in_seq(arr))