import math
def wildlife_population_growth(k,p0,r,t):
    return round(k/(1+(k-p0)/p0*(math.exp(-r*t))))

k=1000
p0=100
r=0.2
t=5

print(wildlife_population_growth(k, p0, r, t))