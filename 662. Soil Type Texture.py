def soil_type_texture(sand, silt, clay):
    if sand>60:
        return "Sandy"
    elif 40<=sand<=60 and (silt+sand)<=40:
        return "Loamey"
    else:
        return "Clay"
    
sand = 70
silt = 20
clay = 10
print(soil_type_texture(sand, silt, clay))