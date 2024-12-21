def maximum_precipitation(precipitation):
    return precipitation.index(max(precipitation))+1

precipitation = [70, 80, 95, 60]
print(maximum_precipitation(precipitation))
