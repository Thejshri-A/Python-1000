def seasonal_temp_change(temps = [5, 7, 15, 20, 25, 30, 35, 32, 28, 20, 10, 5]):
    change=[]
    winter=[temps[11], temps[0], temps[1]]
    spring=temps[2:5]
    summer=temps[5:8]
    fall=temps[8:11]
    seasons=[winter, spring, summer, fall]
    
    for season in seasons:
        change.append(max(season)-min(season))
    return change

print(seasonal_temp_change())