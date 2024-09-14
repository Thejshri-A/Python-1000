def remove_dup(nums):
    no_dup=[]
    no_dup.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i]==nums[i-1]:
            continue
        else:
            no_dup.append(nums[i])
            
    return no_dup

nums=[1,11,11,40,56,56,56,56,67]
print(remove_dup(nums))