def vegetation_health(ndvi = [0.7, 0.4, 0.2]):
    classify=[]
    for val in ndvi:
        if val<0.3:
            classify.append("Not Good")
        elif val<0.6:
            classify.append("Moderate")
        else:
            classify.append("Good")
    return classify

print(vegetation_health())