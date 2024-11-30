def pair_sums_to_target(arr, target):
    seen=set()
    pairs=[]
    
    for num in arr:
        diff=target-num
        if diff in seen:
            pairs.append([diff, num])
        seen.add(num)
    return pairs


arr=[1, 2, 4, 5, 3, 6]
print(pair_sums_to_target(arr, 9))