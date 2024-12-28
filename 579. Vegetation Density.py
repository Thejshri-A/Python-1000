def vegetation_density(ndvi):
    classify=[]
    for val in ndvi:
        if val<0.2:
            classify.append("Sparse")
        elif val<0.5:
            classify.append("Moderate")
        else:
            classify.append("Dense")
    return classify

ndvi = [0.1, 0.3, 0.6]
print(vegetation_density(ndvi))