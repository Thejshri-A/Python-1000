def air_quality_index(C, L, U, I_low, I_high):
    return ((C-L)/(U-L))*(I_high-I_low) + I_low

C = 55
L = 50
U = 100
I_low = 50
I_high = 100
print(air_quality_index(C, L, U, I_low, I_high))