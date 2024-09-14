def merge_intervals(intervals):
    merged = []
    intervals.sort(key=lambda x: x[0])
    print("Intervals are : ", intervals)
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

intervals = [[2, 3], [1, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))