def storm_intensity(speeds):
    classify=[]
    for speed in speeds:
        if 39<=speed<74:
            classify.append("Tropical")
        elif speed>=74:
            classify.append("Hurricane")
        else:
            classify.append("Normal")
    return classify

speeds = [40, 75, 30]
print(storm_intensity(speeds))