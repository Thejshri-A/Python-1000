def deforestation_impact(deforestation, factor):
    return [d*factor for d in deforestation]

deforestation = [10, 20]
factor = 0.1
print(deforestation_impact(deforestation, factor))