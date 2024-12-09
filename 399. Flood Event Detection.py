def flood_event_detection(river_levels, threshold):
    count=0
    for level in river_levels:
        if level>threshold:
            count+=1
            
    return count
    
river_levels = [5, 15, 20, 8]
threshold = 10
print(flood_event_detection(river_levels, threshold))