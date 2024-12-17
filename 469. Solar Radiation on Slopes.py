import math

def solar_radiation_slopes(solar_irradiance, slope_angle):
    return solar_irradiance*math.cos(math.radians(slope_angle))

solar_irradiance = 500
slope_angle = 30
print(solar_radiation_slopes(solar_irradiance, slope_angle))