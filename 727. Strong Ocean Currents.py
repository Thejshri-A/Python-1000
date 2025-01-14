def strong_ocean_current(speeds = [2.5, 3.1, 4.0, 2.8]):
    current=[]
    for speed in speeds:
        if speed>3:
            current.append(speeds.index(speed)+1)
    return current

print(strong_ocean_current())