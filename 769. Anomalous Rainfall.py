def anomalous_rainfall(rainfall = [10, 20, 50, 100, 200]):
    threshold=2*(sum(rainfall)/len(rainfall))
    return [rainfall.index(i) for i in rainfall if i>threshold]

print(anomalous_rainfall())