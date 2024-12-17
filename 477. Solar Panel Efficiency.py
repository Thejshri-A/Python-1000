def solar_panel_efficiency(initial_efficiency, loss_per_degree, temp, temp_ref):
    return initial_efficiency-loss_per_degree*(temp-temp_ref)

initial_efficiency = 20
loss_per_degree = 0.5
temp = 35
temp_ref = 25
print(solar_panel_efficiency(initial_efficiency, loss_per_degree, temp, temp_ref), "%")