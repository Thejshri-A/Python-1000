def desertification_risk(precipitation, potential_evapotranspiration):
    aridity_index=(precipitation/potential_evapotranspiration)
    
    if aridity_index<0.2:
        return "High"
    elif aridity_index<0.5:
        return "Moderate"
    else:
        return "Low"
    
precipitation = 100
potential_evapotranspiration = 400
print(desertification_risk(precipitation, potential_evapotranspiration))