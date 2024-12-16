def vegetation_growth_index(ndvi, ndvi_max, ndvi_min):
    return round((ndvi-ndvi_min)/(ndvi_max-ndvi_min),2)
ndvi = 0.6
ndvi_min = 0.2
ndvi_max = 0.8
print(vegetation_growth_index(ndvi, ndvi_max, ndvi_min))