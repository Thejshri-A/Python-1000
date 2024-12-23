def analyse_air_pollution_trends(pollutants):
    
    if all(pollutants[i]>pollutants[i+1] for i in range(len(pollutants)-1)):
        return "Improving"
    elif all(pollutants[i]<pollutants[i+1] for i in range(len(pollutants)-1)):
        return "Degrading"
    else:
        return "Stable"

pollutants = [50, 45, 40, 32]
print(analyse_air_pollution_trends(pollutants))