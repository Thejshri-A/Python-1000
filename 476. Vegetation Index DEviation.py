def vegetation_index_deviation(ndvi):
    deviations=[]
    for i,val in enumerate(ndvi):
        if val<=0.2:
            deviations.append(i+1)
    return deviations
ndvi = [0.5, 0.3, 0.1, 0.6]
print(vegetation_index_deviation(ndvi))