def water_reservoir_management(initial, inflow, outflow):
    moisture=[initial]
    for i,o in zip(inflow, outflow):
        moisture.append(moisture[-1]+i-o)
    return moisture[1:]

initial = 500
inflow = [100, 200]
outflow = [50, 150]
print(water_reservoir_management(initial, inflow, outflow))