def ground_water_recharge_potential(rainfall, infilteration):
    return [r*i for r,i in zip(rainfall, infilteration)]
rainfall = [200, 300]
infilteration = [0.1, 0.2]
print(ground_water_recharge_potential(rainfall, infilteration))