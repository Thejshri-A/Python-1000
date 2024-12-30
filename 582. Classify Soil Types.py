def classify_soil_types(pH):
    classify=[]
    for val in pH:
        if val<6.5:
            classify.append("Acidic")
        elif val<7.5:
            classify.append("Neutral")
        else:
            classify.append("Alkaline")
    return classify

pH = [5.8, 6.9, 8.2]
print(classify_soil_types(pH))