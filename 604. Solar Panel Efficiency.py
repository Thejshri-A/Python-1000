def solar_panel_efficiency(solar_input, panel_output):
    return f"{(panel_output/solar_input)*100}%"

panel_output = 300
solar_input = 500
print(solar_panel_efficiency(solar_input, panel_output))