def reverse_string(string):
    left, right = 0, len(string)-1
    while left<right:
        string[left], string[right] = string[right], string[left]
        left +=1
        right -=1
    return string
    
        
print(reverse_string(["A", "B", "C", "D"]))