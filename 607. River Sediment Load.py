def river_sediment_load(flow_rate, concentration):
    return flow_rate*concentration

flow_rate = 100
concentration = 0.05
print(river_sediment_load(flow_rate, concentration))