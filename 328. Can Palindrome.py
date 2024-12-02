from collections import Counter
def can_palindrome(string):
    count=Counter(string)
    odd_count = sum(1 for freq in count.values() if freq%2!=0)
    return odd_count<=1

print(can_palindrome("civic"))