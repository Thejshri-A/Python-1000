def humidity_index(temp, rel_hum):
    return temp*rel_hum/100

temp = 30
rel_hum = 70
print(humidity_index(temp, rel_hum))