def land_degradation_severity(erosion_rates):
    classify=[]
    for rate in erosion_rates:
        if rate <5:
            classify.append("Low")
        elif rate<10:
            classify.append("Moderate")
        else:
            classify.append("High")
    return classify

erosion_rates = [3, 7, 12]
print(land_degradation_severity(erosion_rates))