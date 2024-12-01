def binary_count_of_ones(num):
    binary=bin(num)[2:]
    str_bin=str(binary)
    count=sum(1 for s in str_bin if s=="1")
    return count

print(binary_count_of_ones(7))