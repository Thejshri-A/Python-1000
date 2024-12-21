def permafrost_thaw_depth(time, thaw_rate):
    return thaw_rate*(time**0.5)

thaw_rate = 1.5
time = 16
print("Thaw Depth : ",permafrost_thaw_depth(time, thaw_rate), "cm")