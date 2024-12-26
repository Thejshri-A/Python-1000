def evaporation_loss(initial, rate, days):
    evaporation=[initial]
    for i in range(days):
        evaporation.append(evaporation[-1]-evaporation[-1]*rate)
    return evaporation

initial = 100
rate = 0.02
days = 3
print(evaporation_loss(initial, rate, days))