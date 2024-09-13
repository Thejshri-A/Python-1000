def find_triplets(nums):
    nums.sort()  # Sort the list
    triplets = []
    n = len(nums)
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values for i
        
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicate values for j
            
            for k in range(j + 1, n):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue  # Skip duplicate values for k
                
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
    
    return triplets

# Example usage:
num = [-1, 1, 0, 2, 4, -6]
print(find_triplets(num))  # Expected output: [[-6, 2, 4], [-1, 0, 1]]
