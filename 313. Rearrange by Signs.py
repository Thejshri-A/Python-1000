def rearrange(arr):
    positives=[num for num in arr if num>0]
    negatives=[num for num in arr if num<=0]
    return positives+negatives

arr=[1, -4, 22, -4, 6, -5, 8, 10, -45]
print(rearrange(arr))