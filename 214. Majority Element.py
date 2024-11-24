#An array contains elements where one element appears more than n/2 times. 
from collections import Counter

def majority_element(arr):
    
    count = Counter(arr)
    more = len(arr)//2
    for char in arr:
        if count[char]>more:
            return char
    return None
    
arr = [1, 4, 4, 4, 4, 2, 6]
print(majority_element(arr))