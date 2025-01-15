def climate_anomalies(temps = [15.0, 16.1, 15.8, 20.5], mean = 16.0, std_dev = 1.5):
    threshold_up=mean+std_dev
    threshold_down=mean-std_dev
    anomalies=[]
    for val in temps:
        if (val)<threshold_down or (val)>threshold_up:
            anomalies.append(temps.index(val))
            
    return anomalies

print(climate_anomalies())