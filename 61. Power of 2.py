
def isPowerOfTwo(n):
    if n<0:
       return False
    return (n & (n - 1)) == 0

# Example Usage:
n = 16
print(isPowerOfTwo(n))  # Output: True

n = 18
print(isPowerOfTwo(n))  # Output: False
"""

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Example Usage:
n = 16
print(isPowerOfTwo(n))  # Output: True

n = 18
print(isPowerOfTwo(n))  # Output: False
"""