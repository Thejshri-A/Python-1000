from collections import Counter
def reconstruct(arr):
    
    if len(arr)%2!=0:
        return []
    arr.sort()
    count=Counter(arr)
    original=[]
    
    for num in arr:
        if count[num]==0:
            continue
        if count[num*2]==0:
            return []
        original.append(num)
        count[num]-=1
        count[num*2]-=1
    return original

nums = [2, 4, 1, 2, 8, 4]
print(reconstruct(nums))
    