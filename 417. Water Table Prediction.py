def water_table_prediction(initial_water,recharge, discharge):
    levels=[initial_water]
    for r,d in zip(recharge, discharge):
        levels.append(levels[-1]+r-d)
    return levels[1:]

initial_water = 50
recharge = [10, 15]
discharge = [5, 20]
print("Water Table Predicted : ", water_table_prediction(initial_water, recharge, discharge))