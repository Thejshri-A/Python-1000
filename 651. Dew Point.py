def dew_point(temp, humi):
    return temp-((100-humi)/5)

temp = 30
humi = 80
print(dew_point(temp, humi))