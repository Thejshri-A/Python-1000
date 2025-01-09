def wildfire_risk(temperature = 35, humidity = 45):
    if temperature<30 or humidity >50:
        return "Low"
    elif 30<=temperature<=40 and 40<=humidity<=50:
        return "Moderate"
    elif temperature>=40 and humidity<30:
        return "High"

print(wildfire_risk())