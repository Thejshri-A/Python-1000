import math

def tidal_variation_model(height_average, amplitude, period, time):
    height=height_average+amplitude*(math.sin(2*math.pi*period/time))
    
    return f"Tidal Height: {round(height, 2)}"
height_average = 5
amplitude = 2
period = 12
time = 6
print(tidal_variation_model(height_average, amplitude, period, time))