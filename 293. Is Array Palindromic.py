def is_palindromic(arr):
    n=len(arr)
    for i in range( n):
        if arr[i]!=arr[-i-1]:
            return "Not a Palindrome"
        
    return "Yes a Palindrome"

arr=[1, 4, 7, 5, 5, 7, 4, 1]
print(is_palindromic(arr))