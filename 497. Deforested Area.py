def deforested_area(initial, rate, years):
    curr_area=[initial]
    for i in range(years):
        curr_area.append(curr_area[-1]*(1-rate))
        
    return curr_area[-1]
initial = 1000
rate = 0.05
years = 3
print("Remaining Area : ", deforested_area(initial, rate, years))