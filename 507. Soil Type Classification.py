def soil_type_classification(sand, silt, clay):
      
    if sand>60:
        return "Sandy"
    elif silt>40:
        return "Clayey"
    else:
        return "Loamy"

sand = 32
silt = 45
clay = 15
print("Soil Type : ",soil_type_classification(sand, silt, clay))
        