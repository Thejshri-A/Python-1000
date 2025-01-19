def desertification(initial_cover = 70, rate = 0.05, years = 3):
    cover=[initial_cover]
    for i in range(years):
        cover.append(cover[-1]*(1-rate))
    return cover

print(desertification())