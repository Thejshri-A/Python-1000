def merge_subinterval(intervals):
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# Example
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_subinterval(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]