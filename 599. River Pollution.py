def river_pollution(initial_pollution, inflow, outflow):
    pollution=[initial_pollution]
    for i,o in zip(inflow, outflow):
        pollution.append(pollution[-1]+(i-o))
    return pollution

initial_pollution = 50
inflow = [10, 15]
outflow = [5, 10]
print(river_pollution(initial_pollution, inflow, outflow))