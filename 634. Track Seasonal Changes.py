def seasonal_co2(co2_levels = [400, 405, 410, 420, 430, 435, 440, 445, 450, 460, 470, 480]):
    seasons={"Winter": [co2_levels[11], co2_levels[0], co2_levels[1]],
             "Spring":co2_levels[2:5],
             "Summer": co2_levels[5:8],
             "Fall": co2_levels[8:11]}
    averages={season: sum(levels)/len(levels) for season, levels in seasons.items()}
    return averages

print(seasonal_co2())