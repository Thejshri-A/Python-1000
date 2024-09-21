def intersectionArray(nums1, nums2):
    freq={}
    for num in nums1:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    result=[]
    for num in nums2:
        if num in freq and freq[num]>0:
            result.append(num)
            freq[num]-=1
            
    return result

nums1=[1,4,4,5,9]
nums2=[4,  9]
print(intersectionArray(nums1, nums2))