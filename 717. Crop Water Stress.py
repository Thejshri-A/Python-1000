def crop_water_stress(water_supply = [100, 50, 120], threshold = 80):
    classify=[]
    for water in water_supply:
        if water<threshold:
            classify.append("Stressed")
        else:
            classify.append("Not Stressed")
    return classify

print(crop_water_stress())