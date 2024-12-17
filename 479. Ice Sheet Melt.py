def ice_sheet_melt(area, melt_rate, days):
    return area*melt_rate*days

area = 2000
melt_rate = 1.5
days = 365
print("Ice Sheet Melt: ", ice_sheet_melt(area, melt_rate, days))