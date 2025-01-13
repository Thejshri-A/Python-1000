def deforestation_impact(initial_rainfall = 2000, alpha = 30, reduction_factor = 10):
    
    return initial_rainfall-(alpha*reduction_factor)

print(deforestation_impact())