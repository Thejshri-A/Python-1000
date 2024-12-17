def glacier_volume_loss(initial_volume, rate, years):
    curr_volume = [initial_volume]
    for i in range(years):
        curr_volume.append(curr_volume[-1]*(1-rate))
    return curr_volume


initial_volume = 5000
rate = 0.03
years = 3
print(glacier_volume_loss(initial_volume, rate, years))