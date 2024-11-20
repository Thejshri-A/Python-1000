def merge_sorted_arr(nums1, nums2):
    merged_arr = nums1+nums2
    merged_arr.sort()
    return merged_arr

nums1 = [1,2,3]
nums2 = [2,5,6]
print(merge_sorted_arr(nums1, nums2))