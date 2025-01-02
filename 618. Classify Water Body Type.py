def classify_water_body_type(salinity, depth):
    classify=[]
    for sal in salinity:
        if sal<0.5:
            classify.append("Freshwater")
        elif sal<30:
            classify.append("Brackish")
        else:
            classify.append("Saltwater")
    return classify

salinity = [0.3, 15, 35]
depth = [5, 50, 100]
print(classify_water_body_type(salinity, depth))