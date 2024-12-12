def river_sediment_transport(concentration, discharge):
    return [c*d for c,d in zip(concentration,discharge)]

concentration = [50, 100]
discharge = [200, 300]
print(river_sediment_transport(concentration, discharge))