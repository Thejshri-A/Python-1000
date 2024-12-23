def predict_renewable_energy_growth(capacity, growth_rate , years):
    energy_growth=[capacity]
    for i in range(years):
        energy_growth.append(energy_growth[-1]*(1+growth_rate))
    return energy_growth

capacity = 100
growth_rate = 0.15
years = 3
print(predict_renewable_energy_growth(capacity, growth_rate, years))