def air_quality_index(aqi_val):
    classifications=[]
    
    for val in aqi_val:
        if 0<val<=50:
            classifications.append("Good")
        elif 50<val<=100:
            classifications.append("Moderate")
        else:
            classifications.append("Not Good")
    return classifications

aqi_val=[45, 90, 150]
print(air_quality_index(aqi_val))