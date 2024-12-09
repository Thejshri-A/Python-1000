def calculate_vegetation_health(ndvi):
    classification=[]
    for val in ndvi:
        if val<0.2:
            classification.append("Low")
        elif val<=0.5:
            classification.append("Moderate")
        elif 0.5<val<=1.0:
            classification.append("Healthy")
        else:
            classification.append("Are you Sure?")
            
    return classification

ndvi = [0.1, 0.3, 0.6]
print(calculate_vegetation_health(ndvi))

