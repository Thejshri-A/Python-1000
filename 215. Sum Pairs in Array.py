#To find all unique pairs of numbers in an array that sum up to a given value.

def sum_pairs(arr, target):
    seen= set()
    pairs = []
    
    for num in arr:
        complement = target-num
        if complement in seen:
            pairs.append((num, complement))
        else:
            seen.add(num)
    return pairs
    
    
arr = [2, 4, 3, 5, 7, 8, 1]
target = 8       
print(sum_pairs(arr, target))    