def sea_level_rise(melt_rate = 0.02, volume_per_unit = 10, years = 5):
    return melt_rate*volume_per_unit*years

print(sea_level_rise())