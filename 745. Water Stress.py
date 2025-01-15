def water_stress(moisture = [25, 45, 70]):
    classify=[]
    for val in moisture:
        if val<30:
            classify.append("Severe")
        elif val<60:
            classify.append("Moderate")
        else:
            classify.append("Normal")
    return classify

print(water_stress())