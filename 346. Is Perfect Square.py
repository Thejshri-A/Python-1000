def is_perfect_square(num):
    left, right = 1, num
    while left<=right:
        mid=(left+right)//2
        if mid*mid==num:
            return True
        elif mid*mid<num:
            left=mid+1
        else:
            right=mid-1
    return False

print(is_perfect_square(625))
            