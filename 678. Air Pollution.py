def air_pollution(aqi = [45, 80, 120]):
    classify=[]
    for val in aqi:
        if val<50:
            classify.append("Good")
        elif val<100:
            classify.append("Moderate")
        else:
            classify.append("Not Good")
    return classify
    
print(air_pollution())