def river_flood_peaks(river_flow, threshold):
    peaks=[]
    for i in range(1, len(river_flow)):
        if river_flow[i]>threshold and river_flow[i-1]<river_flow[i]>river_flow[i+1]:
            peaks.append(river_flow[i])
            
    return peaks

river_flow = [50, 120, 150, 80, 200, 220, 180]
threshold = 100
print(river_flood_peaks(river_flow, threshold))