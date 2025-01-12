def vegetation_types(temperature = [16, 12, 22], precipitation = [1200, 700, 300]):
    classify=[]
    for temp, precip in zip(temperature, precipitation):
        if temp>15 and precip>1000:
            classify.append("Forest")
        elif 10<=temp<=15 and 500<=precip<=1000:
            classify.append("Grasslands")
        elif temp>20 and precip<500:
            classify.append("Desert")
        else:
            classify.append("Not classified")
    return classify

print(vegetation_types())