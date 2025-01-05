def extreme_temperature(temperatures):
    classify=[]
    for temp in temperatures:
        if temp>40:
            classify.append("Extreme Hot")
        elif 10<temp<40:
            classify.append("Normal")
        else:
            classify.append("Extreme Cold")
    return classify

temperatures = [5, 20, 45, 8, 39]
print(extreme_temperature(temperatures))