def rainfall_anomalies(rainfall, avg):
    classify=[]
    for rain in rainfall:
        if rain<avg:
            classify.append("Below")
        elif rain==avg:
            classify.append("Normal")
        else:
            classify.append("Above")
    return classify

rainfall = [30, 50, 80]
avg = 50
print(rainfall_anomalies(rainfall, avg))