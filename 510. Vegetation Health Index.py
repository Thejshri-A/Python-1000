def vegetation_health_index(ndvi, evi):
    return ndvi-0.5*evi

ndvi = 0.8
evi = 0.6
print("Vegetation Health Index :", vegetation_health_index(ndvi, evi))