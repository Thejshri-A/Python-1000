def temperature_anomalies(temps):
    monthly_average=[sum(temps[i:i+30])/30 for i in range(0, len(temps), 30)]
    annual_average=sum(monthly_average)/len(monthly_average)
    temp_anomalies = [round(month-annual_average,2) for month in monthly_average]
    return temp_anomalies

import random
daily_temps= [random.randint(15,35) for _ in range(365)]
print(temperature_anomalies(daily_temps))