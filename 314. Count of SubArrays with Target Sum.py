def count_of_subArrays_with_sum(arr, target):
    count=0
    prefix_sum={0:1}
    current_sum=0
    for num in arr:
        current_sum+=num
        if current_sum-target in prefix_sum:
            count+=prefix_sum[current_sum-target]
        prefix_sum[current_sum]=prefix_sum.get(current_sum, 0)+1
    return count

# Example Usage
arr = [1, 1, 1]
target = 2
print(count_of_subArrays_with_sum(arr, target))  # Output: 2