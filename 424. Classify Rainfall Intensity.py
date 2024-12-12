def classify_rainfall_intensity(rainfall):
    classification={}
    
    for rain in rainfall:
        if rain<10:
            classification[rain]="Low"
        elif 10<=rain<=50:
            classification[rain]="Moderate"
        else:
            classification[rain]="High"
    return classification

rainfall=[5, 18, 150]
print(classify_rainfall_intensity(rainfall))