def insertInterval(intervals, new_interval):
    result = []
    for i in intervals:
        if i[1] < new_interval[0]:
            result.append(i)
        elif i[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = i
        else:
            new_interval = [min(i[0],new_interval[0]), max(i[1], new_interval[1])]
        
    result.append(new_interval)
        
    return result

# Example:
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insertInterval(intervals, new_interval))  # Output: [[1, 5], [6, 9]]