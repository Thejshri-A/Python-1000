def drought_recovery_years(rainfall, threshold):
    years=[]
    for i,rain in enumerate(rainfall):
        if rain>threshold:
            years.append(i+1)
    return years

rainfall = [200, 300, 500]
threshold = 400
print(drought_recovery_years(rainfall, threshold))