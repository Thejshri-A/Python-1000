def climate_zones(temperature = [20, 15, 8], precipitation = [80, 40, 70]):
    classify=[]
    for temp, precip in zip(temperature, precipitation):
        if temp>18 and precip>60:
            classify.append("Tropical")
        elif precip<60:
            classify.append("Dry")
        elif 10<=temp<=18:
            classify.append("Temperate")
    return classify

print(climate_zones())