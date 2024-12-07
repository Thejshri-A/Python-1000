def cel_kel(temps):
    return [round(temp+273.15,2) for temp in temps]

temps = [0, 25, 100]
print(cel_kel(temps))