def rainwater_harvesting_potential(rooftop, rainfall, collection_efficiency):
    return rooftop*rainfall*collection_efficiency

rooftop = 100
rainfall = 200
collection_efficiency = 0.8
print(rainwater_harvesting_potential(rooftop, rainfall, collection_efficiency), " litres")