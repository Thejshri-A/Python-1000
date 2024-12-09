def classify_climate_zones(temps):
    classifications=[]
    for temp in temps:
        if temp<0:
            classifications.append("Arctic")
        elif temp<20:
            classifications.append("Temperate")
        else:
            classifications.append("Tropical")
            
    return classifications

temps = [-5, 15, 25]
print(classify_climate_zones(temps))
    