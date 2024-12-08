def ocean_acidification(ph_values, threshold):
    return sum(ph<threshold for ph in ph_values)

ph_values = [8.0, 7.5, 7.8, 7.6]
threshold=7.8
print(ocean_acidification(ph_values, threshold))