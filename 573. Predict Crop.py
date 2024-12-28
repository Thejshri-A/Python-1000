def predict_crop(initial_yield, rate, years):
    crop_yield=[initial_yield]
    for i in range(years):
        crop_yield.append(crop_yield[-1]*(1+rate))
    return crop_yield

initial_yield = 1000
rate = 0.05
years = 3
print(predict_crop(initial_yield, rate, years))