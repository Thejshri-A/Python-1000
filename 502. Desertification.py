def desertification_risk(rainfall_level):
    classify=[]
    for level in rainfall_level:
        if level<250:
            classify.append("High")
        elif level<500:
            classify.append("Moderate")
        elif 500<=level:
            classify.append("Low")
        else:
            classify.append(" ")
    return classify

rainfall_level = [200, 300, 600]
print(desertification_risk(rainfall_level))