def monthly_average_temperature(temps, no_of_days):
    average = [sum(temps[i:i+no_of_days])/no_of_days for i in range(0, len(temps), no_of_days)]
    return average

temps = [30, 31, 32, 28, 27, 29]
print(monthly_average_temperature(temps, 2))