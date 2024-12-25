def ice_sheet_melting(initial_volume, rate, years):
    volume=[initial_volume]
    for i in range(years):
        volume.append(volume[-1]-rate)
    return volume

initial_volume = 2000
rate = 100
years = 4
print(ice_sheet_melting(initial_volume, rate, years))