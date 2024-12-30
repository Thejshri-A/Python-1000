def crop_irrigation_requirement(crop_water_demand, rainfall):
    return [d-r for d,r in zip(crop_water_demand, rainfall)]

crop_water_demand = [50, 60]
rainfall = [20, 30]
print("Irrigation Needs : ", crop_irrigation_requirement(crop_water_demand, rainfall))