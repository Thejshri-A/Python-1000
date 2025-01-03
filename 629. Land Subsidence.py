def land_subsidence(initial_subsidence, withdrawal_rate, years):
    subsidence=[initial_subsidence]
    for i in range(1,years+1):
        subsidence.append(subsidence[0] + (withdrawal_rate*i))
    return subsidence

initial_subsidence = 0
withdrawal_rate = 1
years = 3
print(land_subsidence(initial_subsidence, withdrawal_rate, years))