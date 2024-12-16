def glacier_meltwater_contribution(glacier_area, melt_rate, days):
    return glacier_area*melt_rate*days/1000

glacier_area = 10
melt_rate = 5
days = 150
print(glacier_meltwater_contribution(glacier_area, melt_rate, days))