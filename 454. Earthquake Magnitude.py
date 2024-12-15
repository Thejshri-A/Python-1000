def earthquake_magnitude(magnitudes):
    classifications={"Minor":0, "Moderate":0, "Major":0}
    
    for mag in magnitudes:
        if mag<=4:
            classifications["Minor"]+=1
        elif mag<=6:
            classifications["Moderate"]+=1
        elif 6<mag:
            classifications["Major"]+=1
    return classifications

magnitudes = [3.5, 4.2, 6.5, 5.0]
print(earthquake_magnitude(magnitudes))