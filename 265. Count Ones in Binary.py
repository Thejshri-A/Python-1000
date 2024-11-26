def count_ones_in_binary(num):
    binary= bin(num)
    count=0
    binary_str = str(binary)
    
    for b in binary_str:
        if b=="1":
            count+=1
    return count

print(count_ones_in_binary(9))