def Hamming_distance(x,y):
    return bin(x^y).count("1")

print(Hamming_distance(1, 4))