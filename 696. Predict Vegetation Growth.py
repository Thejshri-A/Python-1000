def predict_vegetation_growth(initial_population = 100, growth_rate = 0.1, capacity = 1000, years = 3):
    popul=[initial_population]
    for i in range(years):
        popul.append(popul[-1]+growth_rate*popul[-1]*(1-(popul[-1]/capacity)))
    return popul
print(predict_vegetation_growth())