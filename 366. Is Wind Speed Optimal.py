def is_wind_speed_optimal(speeds):
    return sum(12<=speed<=25 for speed in speeds)
speeds = [10, 15, 22, 30, 18]
print(is_wind_speed_optimal(speeds))