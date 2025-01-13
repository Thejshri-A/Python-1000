def soil_nutrient(initial_nutrient = 50, incoming = [10, 15], depletion = [5, 8]):
    nutrient=[initial_nutrient]
    for i,d in zip(incoming, depletion):
        nutrient.append(nutrient[-1]+i-d)
    return nutrient

print(soil_nutrient())