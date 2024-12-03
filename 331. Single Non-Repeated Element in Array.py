def single_non_repeat(arr):
    result=0
    for num in arr:
        result^=num
    return result

nums = [4, 1, 2, 1, 2]
print(single_non_repeat(nums))