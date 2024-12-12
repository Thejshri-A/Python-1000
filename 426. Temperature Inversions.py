def temperature_inversions(temperatures, altitudes):
    
    """
    Given temperature readings at different altitudes, identify inversion layers where temperature increases with altitude.
Example:
Input: temperatures = [20, 18, 19, 21, 20], altitudes = [0, 1, 2, 3, 4]
    """
    inversion_layers=[]
    
    for i in range(1,len(temperatures)):
        if temperatures[i]>temperatures[i-1]:
            inversion_layers.append((altitudes[i-1],altitudes[i]))
    return inversion_layers

temperatures = [20, 18, 19, 21, 20]
altitudes = [0, 1, 2, 3, 4]

print(temperature_inversions(temperatures, altitudes))