def median(arr):
    if len(arr)%2==1:
        return arr[len(arr)//2]
    else:
        return (arr[(len(arr)//2)]+arr[((len(arr)//2)-1)])/2
arr=[1, 2, 3, 4, 5, 6]
print(median(arr))