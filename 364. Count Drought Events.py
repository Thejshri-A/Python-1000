def count_drought_events(precip):
    min_precip = 50
    count=0
    for i in range(1, len(precip)):
        if precip[i]<min_precip and precip[i-1]<min_precip:
            count+=1
    
    return count

precip = [60, 45, 30, 80, 20, 10]
print(count_drought_events(precip))