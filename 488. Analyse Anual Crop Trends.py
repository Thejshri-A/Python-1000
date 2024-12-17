def analyse_annual_crop_trends(yields):
    
    if all(yields[i]<yields[i+1] for i in range(len(yields)-1)):
        return "Increasing"
    elif all(yields[i]>yields[i+1] for i in range(len(yields)-1)):
        return "Decreasing"
    else:
        return "Stable"
yields = [200, 210, 190, 220]  
print(analyse_annual_crop_trends(yields))