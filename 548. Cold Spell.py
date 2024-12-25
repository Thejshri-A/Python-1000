def cold_spell(temps, threshold):
    cold=[]
    start=None
    for i, val in enumerate((temps)):
        if val<threshold:
            if start is None:
                start=i+1
        else:
            if start is not None:
                cold.append([start, i])
                start=None
    if start is not None:
        cold.append([start, len(temps)])
    return cold

    
temps = [5, -2, -3, 4, -1]
threshold = 0
print(cold_spell(temps, threshold))