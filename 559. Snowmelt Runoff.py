def snowmelt_runoff(snow_melt, efficiency):
    return snow_melt*efficiency

snow_melt = 50
efficiency = 0.8
print("Snowmelt : ", snowmelt_runoff(snow_melt, efficiency))