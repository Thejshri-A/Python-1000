def forest_fire_risk_areas(temp, humidity, wind_speed):
    if temp<30 and humidity>50:
        return "Low Risk"
    if temp>=30 or wind_speed>20:
        return "High Risk"

temp = 35
humidity = 40
wind_speed = 25
print(forest_fire_risk_areas(temp, humidity, wind_speed))