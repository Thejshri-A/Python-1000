def max_xor_of_two_numbers(nums):
    max_xor_val=0
    mask=0
    for i in range(31, -1, -1):
        mask|=(1<<i)
        prefixes={num&mask for num in nums}
        temp=max_xor_val|(1<<i)
        if any(temp^prefix in prefixes for prefix in prefixes):
            max_xor_val=temp
    return max_xor_val
# Example Usage
nums = [3, 10, 5, 25, 2, 8]
print(max_xor_of_two_numbers(nums))  # Output: 28