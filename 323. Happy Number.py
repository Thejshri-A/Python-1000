def isHappy(number):
    
    def get_next(num):
        return sum(int(digit)**2 for digit in str(num))
    slow=fast=1
    while fast!=1 and get_next(fast)!=1:
        slow=get_next(slow)
        fast=get_next(get_next(fast))
        if slow==fast:
            return False
    return True

print(isHappy(125))