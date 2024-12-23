def classify_temperatures(temps):
    classify=[]
    for temp in temps:
        if temp<10:
            classify.append("Cold")
        elif temp<25:
            classify.append("Moderate")
        elif temp<50:
            classify.append("Hot")
        else:
            classify.append("")
    return classify

temps = [5, 15, 30]
print(classify_temperatures(temps))