def ndvi_vegetation_metric(ndvi = [0.2, 0.5, 0.7]):
    classify=[]
    for val in ndvi:
        if val<0.3:
            classify.append("Not Good")
        elif val<0.6:
            classify.append("Moderate")
        else:
            classify.append("Good")
    return classify

print(ndvi_vegetation_metric())