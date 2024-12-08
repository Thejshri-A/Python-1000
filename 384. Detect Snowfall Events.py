def snowfall_events(precipitation, temperature):
    return sum(p>0 and t<0 for p,t in zip(precipitation, temperature))

precipitation = [10, 0, 20, 5]
temperature = [2, -1, -3, 5]

print(snowfall_events(precipitation, temperature))