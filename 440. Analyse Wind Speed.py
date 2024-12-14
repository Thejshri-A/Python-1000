def analyse_wind_speed(wind_speeds):
    north_south = 0
    east_west = 0
    total=len(wind_speeds)
    
    for u,v in wind_speeds:
        north_south+=abs(v)
        east_west+=abs(u)
    
    north_south_average=north_south/total
    east_west_average = east_west/total
    
    return north_south_average, east_west_average

wind_speeds=[(10, 5), (-10, -5)]
north_south_average,east_west_average=analyse_wind_speed(wind_speeds)
print(f"North South : {north_south_average}, East West : {east_west_average}")