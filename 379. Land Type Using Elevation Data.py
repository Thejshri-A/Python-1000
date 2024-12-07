def classify_land(elevation_data):
    classification=[]
    
    for elevation in elevation_data:
        
        if elevation<200:
            classification.append("Plain")
        elif elevation<1000:
            classification.append("Hill")
        elif elevation<=1500:
            classification.append("Mountain")
        else:
            classification.append("Are you Flying in Atmosphere?")
            
    return classification
elevation_data = [100, 500, 1500]

print(classify_land(elevation_data))
