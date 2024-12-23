def above_avg_solar_irradiance(irradiance):
    avg_irradiance=sum(irradiance)/len(irradiance)
    above_avg_irradiance=[]
    for i, val in enumerate(irradiance):
        if val>avg_irradiance:
            above_avg_irradiance.append(i+1)
    return above_avg_irradiance

irradiance = [300, 500, 400]
print(above_avg_solar_irradiance(irradiance))