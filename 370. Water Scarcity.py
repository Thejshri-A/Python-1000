def water_scarcity(levels, threshold):
    count=0
    for level in levels:
        if level<threshold:
            count+=1
    return count


    
levels = [120, 80, 150, 90, 70]
threshold = 100

print(water_scarcity(levels, threshold))