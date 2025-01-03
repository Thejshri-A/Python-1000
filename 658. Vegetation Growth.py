def vegetation_growth(ndvi):
    if all(ndvi[i]>ndvi[i-1] for i in range(1, len(ndvi))):
        return "Increasing"
    elif all(ndvi[i]<ndvi[i-1] for i in range(1, len(ndvi))):
        return "Descreasing"
    else:
        return "No Specific Trend"

ndvi = [0.4, 0.5, 0.6, 0.7]
print(vegetation_growth(ndvi))