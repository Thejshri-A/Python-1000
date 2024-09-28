def binary_add(a, b):
    return bin(int(a, 2)+ int(b, 2))[2:]

# Example
a = "1010"
b = "1011"
print(binary_add(a, b))