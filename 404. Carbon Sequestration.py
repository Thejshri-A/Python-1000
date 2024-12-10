def carbon_sequestration(forest_area, sequestration_rate, years):
    return forest_area*sequestration_rate*years

forest_area = 500 
sequestration_rate = 2
years = 10
print("Sequestration Rate is : ", carbon_sequestration(forest_area, sequestration_rate, years))