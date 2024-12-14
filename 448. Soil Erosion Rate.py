def soil_erosion_rate(k, ls, c, p):
    return k*ls*c*p

k = 0.3
ls = 2
c = 0.5
p = 1
print("Soil Erosion : ", soil_erosion_rate(k, ls, c, p))