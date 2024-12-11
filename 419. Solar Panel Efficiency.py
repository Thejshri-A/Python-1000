def solar_panel_efficiency(daily_solar_radiation, panel_area, efficiency):
    return [round(daily*panel_area*efficiency,2) for daily in daily_solar_radiation]

daily_solar_radiation = [5, 6]
panel_area = 10
efficiency = 0.2
print(solar_panel_efficiency(daily_solar_radiation, panel_area, efficiency))