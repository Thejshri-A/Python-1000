def coastal_erosion(initial_length = 100, rate = 2, years = 5):
    length=[initial_length]
    for i in range(years):
        length.append(length[-1]-rate)
    return length

print(coastal_erosion())