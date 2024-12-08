def classify_storm(storm_values):
    """
    - Tropical Depression: <63
- Tropical Storm: 63–118
- Category 1: 119–153
- Category 2: 154–177
    """
    classifications=[]
    for storm in storm_values:
        if storm <63:
            classifications.append("Tropical Depression")
        elif storm<118:
            classifications.append("Tropical Storm")
        elif storm<153:
            classifications.append("Category 1")
        elif storm<177:
            classifications.append("Category 2")
        else:
            classifications.append("NAN")
            
    return classifications
storm_values = [60, 120, 160]
print(classify_storm(storm_values))