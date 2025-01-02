def iceberg_salinity(salinity, threshold):
    classify=[]
    for val in salinity:
        if val<threshold:
            classify.append("Iceberg")
        else:
            classify.append("Normal")
    return classify

salinity = [30, 35, 28, 34]
threshold = 32
print(iceberg_salinity(salinity, threshold))