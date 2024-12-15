def evapotranspiration(net_radiation, soil_heat, latent_heat):
    return round((net_radiation-soil_heat)/latent_heat,2)

net_radiation = 200
soil_heat = 50
latent_heat = 2.45
print("Evapotranspiration : ", evapotranspiration(net_radiation, soil_heat, latent_heat))