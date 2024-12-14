def solar_panel_efficiency(area, irradiance, efficiency):
    return area*irradiance*efficiency
area = 10
irradiance = 500
efficiency = 0.2
print("Energy : ",solar_panel_efficiency(area, irradiance, efficiency), " W")