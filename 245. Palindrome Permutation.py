from collections import Counter

def palindrome_permutation(s):
    s=s.replace(" ", "").lower()
    count=Counter(s)
    
    odd_count=sum(1 for val in count.values() if val%2==1)
    
    return odd_count<=1

s="taco catg"
print(palindrome_permutation(s))