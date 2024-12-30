def co2_absorption_by_ocean(initial_absorption, rates):
    absorption=[initial_absorption]
    for rate in rates:
        absorption.append(absorption[-1]+rate)
    return absorption
initial_absorption = 100
rates = [5, 7, 6]
print(co2_absorption_by_ocean(initial_absorption, rates))