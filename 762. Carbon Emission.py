def carbon_emission(fuel = [10, 15], factor = 2.31):
    return [f*factor for f in fuel]

print(carbon_emission())