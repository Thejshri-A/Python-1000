def groundwater_withdrawal_impact(water_withdrawal, aquifer_area):
    return water_withdrawal/(aquifer_area*1000000)

water_withdrawal=100000
aquifer_area = 50
print(groundwater_withdrawal_impact(water_withdrawal, aquifer_area))