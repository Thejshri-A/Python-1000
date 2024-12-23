def co2_accumulation(initial_concentration, emissions, absorption , years):
    concentration=[initial_concentration]
    for i in range(years):
        concentration.append(concentration[-1]+(emissions-absorption))
    return concentration

initial_concentration = 400
emissions = 20
absorption = 15
years = 3
print(co2_accumulation(initial_concentration, emissions, absorption , years))