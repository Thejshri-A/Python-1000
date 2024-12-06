def NDVI_calculation(nir, red):
    ndvi=[]
    for i in range(len(nir)):
        curr_ndvi=((nir[i] - red[i])/(nir[i] + red[i]))
        ndvi.append(curr_ndvi)
        
    return ndvi

nir = [0.7, 0.8]
red = [0.3, 0.4]

print(NDVI_calculation(nir, red))