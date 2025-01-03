def identify_urban_zones(land_use):
    urban=[]
    
    for i,val in enumerate(land_use):
        if val=="Urban":
            urban.append(i+1)
    return urban

land_use = ['Forest', 'Urban', 'Urban', 'Forest']
print(identify_urban_zones(land_use))