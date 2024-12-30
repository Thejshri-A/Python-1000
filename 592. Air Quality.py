def air_quality(aqi):
    classify=[]
    for val in aqi:
        if val<50:
            classify.append("Good")
        elif val<100:
            classify.append("Moderate")
        else:
            classify.append("Not Good")
    return classify
aqi = [45, 75, 120]
print(air_quality(aqi))