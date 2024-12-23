def identify_drought_years(rainfall, threshold):
    drought=[]
    for i,rain in enumerate(rainfall):
        if rain<threshold:
            drought.append(i+1)
    return drought

rainfall = [800, 600, 500, 900]
threshold = 700
print("Drought Years : ", identify_drought_years(rainfall, threshold))