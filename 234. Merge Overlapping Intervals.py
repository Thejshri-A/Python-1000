def merge_overlapping_intervals(intervals):
    merged_intervals=[]
    intervals.sort(key= lambda x:x[0])
    
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1]< interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1]=interval[1]
    return merged_intervals

# Example Usage
intervals = [[1, 3], [2, 6], [8, 16], [15, 18]]
print(merge_overlapping_intervals(intervals))