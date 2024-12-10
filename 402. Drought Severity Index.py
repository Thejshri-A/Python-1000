import statistics

def drought_severity_index(rainfall):
    mean_rainfall = statistics.mean(rainfall)
    std_dev_rainfall = statistics.stdev(rainfall)
    return [round((r-mean_rainfall)/std_dev_rainfall,2) for r in rainfall]

rainfall = [20, 40, 60, 80, 100, 120, 140, 100, 80, 60, 40, 20]
print(drought_severity_index(rainfall))