def air_quality(aqi_values = [45, 80, 150]):
    classify=[]
    for aqi in aqi_values:
        if aqi<50:
            classify.append("Good")
        elif aqi<100:
            classify.append("Moderate")
        else:
            classify.append("Polluted")
    return classify

print(air_quality())