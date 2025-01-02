import numpy as np

def rainfall_variability(rainfall):
    std_dev = np.std(rainfall)
    return f"Standard Deviation Of Rainfall : {std_dev:.1f}"

rainfall = [100, 120, 80, 150, 130]
print(rainfall_variability(rainfall))