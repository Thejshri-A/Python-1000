def precipitation_intensity(precipitation):
    classify=[]
    for val in precipitation:
        if val<2:
            classify.append("Light")
        elif val<10:
            classify.append("Moderate")
        else:
            classify.append("Heavy")
    return classify

precipitation = [1.5, 8, 12]
print(precipitation_intensity(precipitation))