def air_quality_index(aqi):
    classify=[]
    for val in aqi:
        if val<50:
            classify.append("Clean")
        elif val<100:
            classify.append("Moderate")
        else:
            classify.append("Not Clean")
    return classify

aqi = [30, 70, 120]
print(air_quality_index(aqi))