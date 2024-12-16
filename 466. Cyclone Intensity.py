"""Given wind speeds, classify cyclones using the Saffir-Simpson scale:
- Category 1: 74−95mph
- Category 2: 96−110mph
- Category 3: 111−129mph
"""
def saffir_simpson_scale(cyclone_intensities):
    scale=[]
    for intensity in cyclone_intensities:
        if 74<=intensity<=95:
            scale.append("Category 1")
        
        elif 96<=intensity<=110:
            scale.append("Category 2")
        
        
        elif 111<=intensity<=129:
            scale.append("Category 3")
            
        else:
            scale.append("Check the value!")
    return scale

cyclone_intensities = [80, 100, 120]
print(saffir_simpson_scale(cyclone_intensities))