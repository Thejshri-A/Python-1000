def classify_earthquake(magnitudes):
    
    classifications=[]
    
    for magnitude in magnitudes:
        
        if magnitude<4.0:
            classifications.append("Minor")
        elif 4.0<=magnitude<4.9:
            classifications.append("Light")
        elif 4.9<=magnitude<5.9:
            classifications.append("Moderate")
        elif 5.9<=magnitude:
            classifications.append("Strong")
        else:
            classifications.append("Not Valid")
    return classifications

magnitudes = [3.5, 4.2, 5.5, 6.1]
print(classify_earthquake(magnitudes))