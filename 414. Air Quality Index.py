def air_quality_index(aqi_values):
    classifications=[]
    for val in aqi_values:
        
        if 0<=val<=50:
            classifications.append("Good")
        elif 51<=val<=100:
            classifications.append("Moderate")
        elif 101<=val<=250:
            classifications.append("Unhealthy")
        else:
            classifications.append("Are you sure?")
    return classifications

aqi_values = [40, 80, 120]
print("Classifications : ", air_quality_index(aqi_values))