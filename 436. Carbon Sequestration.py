def carbon_sequetration(forest_area, sequestration_rate):
    return [area*sequestration_rate for area in forest_area]
forest_area = [100, 200]
sequestration_rate = 5
print("Carbon Sequestration : ", carbon_sequetration(forest_area, sequestration_rate))