def seasonal_snow_melt(temperatures = [0, 5, -2, 8], threshold = 0):
    melt=[]
    for temp in temperatures:
        melt.append(max(0, temp-threshold))
    return melt

print(seasonal_snow_melt())