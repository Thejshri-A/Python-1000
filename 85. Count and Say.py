def countAndSay(n):
    result="1"
    for _ in range(n-1):
        next_result = ""
        count = 1
        for j in range(1, len(result)):
            if result[j] == result[j-1]:
                count +=1
            else:
                next_result += str(count) + result[j-1]
                count =1
        next_result += str(count) + result[-1]
        result = next_result
    return result

n=4
print(countAndSay(n))