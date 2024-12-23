def sea_level_rise(rates):
    cumulative_rise=[rates[0]]
    for rate in rates[1:]:
        cumulative_rise.append(cumulative_rise[-1]+rate)
    return cumulative_rise

rates = [2, 3, 1.5, 2.5]
print(sea_level_rise(rates))