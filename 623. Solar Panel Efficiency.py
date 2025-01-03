def solar_panel_efficiency(initial_efficiency, rate, years):
    eff=[initial_efficiency]
    for i in range(years):
        eff.append(eff[-1]*((1-rate)))
    return eff

initial_efficiency = 100
rate = 0.02
years = 3
print(solar_panel_efficiency(initial_efficiency, rate, years))