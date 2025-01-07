def extreme_precipitation(precipitation = [10, 20, 50, 5], threshold = 30):
    extremes=[]
    for i,val in enumerate(precipitation):
        if val>30:
            extremes.append(i+1)
    return extremes

print(extreme_precipitation())