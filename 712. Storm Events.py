def storm_events(wind_speeds = [30, 55, 60, 40, 70]):
    storm=[]
    threshold=50
    for wind in wind_speeds:
        if wind>threshold:
            storm.append(wind_speeds.index(wind)+1)
    return storm

print(storm_events())