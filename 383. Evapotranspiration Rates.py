def evaporation_rate(kc, radiation):
    return [round(val*kc,2) for val in radiation]
    
kc = 0.8
radiation = [5, 6, 7]
print(evaporation_rate(kc, radiation))