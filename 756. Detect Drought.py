def detect_drought(rainfall = [400, 200, 100, 300], threshold = 250):
    drought=[]
    for rain in rainfall:
        if rain<threshold:
            drought.append(rainfall.index(rain))
    return drought

print(detect_drought())
        