def cyclone_intensity(pressure_data):
    classifications=[]
    for data in pressure_data:
        if data<=950:
            classifications.append("Severe Cyclone")
        elif 950<=data<=980:
            classifications.append("Cyclonic Storm")
        elif data>980:
            classifications.append("Tropical Depression")
        else:
            classifications.append("Are you sure?")
    
    return classifications

pressure_data = [985, 960, 940]
print(cyclone_intensity(pressure_data))