def urban_air_quality_index(aqi_val):
    classify=None
    
    if 0<=aqi_val<=50:
        classify="Good"
    elif 51<=aqi_val<=100:
        classify="Moderate"
    elif 101<=aqi_val<=150:
        classify="Bad"
    elif 151<=aqi_val:
        classify="Very Bad"
    else:
        classify="Check the value"
    return classify

aqi_val = 120
print(urban_air_quality_index(aqi_val))