def rainfall_intensity(rainfall):
    classify=[]
    for rain in rainfall:
        if rain<10:
            classify.append("Light")
        elif rain<25:
            classify.append("Moderate")
        else:
            classify.append("Heavy")
    return classify

rainfall = [5, 15, 30]
print(rainfall_intensity(rainfall))