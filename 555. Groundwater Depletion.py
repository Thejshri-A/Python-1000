def groundwater_depletion(initial_groundwater, withdrawal):
    depletion=[initial_groundwater]
    for i in range(len(withdrawal)):
        depletion.append(depletion[-1]-withdrawal[i])
    return depletion

initial_groundwater = 500
withdrawal = [50, 60, 70]
print(groundwater_depletion(initial_groundwater, withdrawal))