def soil_type_permeability(rates = [12, 8, 3]):
    classify=[]
    for rate in rates:
        if rate>10:
            classify.append("High")
        elif rate>5:
            classify.append("Moderate")
        else:
            classify.append("Low")
    return classify
    
print(soil_type_permeability())