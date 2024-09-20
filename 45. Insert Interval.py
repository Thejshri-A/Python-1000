def insertIntervals(intervals, new_interval):
    merged = []
    for i in range(len(intervals)):
        if intervals[i][1]<new_interval[0]:
            merged.append(intervals[i])
        elif intervals[i][0]>new_interval[1]:
            merged.append(new_interval)
            return merged+intervals[i:]
        else:
            new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
    
    merged.append(new_interval)
    return merged

# Example
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insertIntervals(intervals, newInterval))  # Output: [[1, 5], [6, 9]]