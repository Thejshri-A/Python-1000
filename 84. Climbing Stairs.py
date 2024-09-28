def climbStairs(num):
    if num <=2:
        return num
    first, second = 1, 2
    for i in range(3, num+1):
        first, second = second, first+second
    return second

num=5
print(climbStairs(num))