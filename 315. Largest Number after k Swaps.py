def largest_number_after_k_swaps(num, k):
    num=list(num)
    
    def helper(index, k):
        if k==0 or index==len(num):
            return
        max_digit=max(num[index:])
        if max_digit==num[index]:
            helper(index+1, k)
            return
        for i in range(index, len(num)):
            if num[i]==max_digit:
                num[index], num[i] =num[i], num[index]
                helper(index+1, k-1)
                #num[index], num[i] =num[i], num[index]
               
        
    helper(0, k)
    return "".join(num)

num="2736"
k=2
print(largest_number_after_k_swaps(num, k))
