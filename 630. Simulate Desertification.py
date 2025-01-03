def simulate_desertification(initial_area, rate, years):
    return [initial_area+(rate*t) for t in range(years+1)]

initial_area = 100
rate = 10
years = 3
print(simulate_desertification(initial_area, rate, years))