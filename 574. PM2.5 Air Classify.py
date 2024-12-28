def pm2_5_air_classify(concentrations):
    classify=[]
    for concentration in concentrations:
        if concentration<50:
            classify.append("Good")
        elif concentration<100:
            classify.append("Moderate")
        else:
            classify.append("Not Good")
    return classify

concentrations = [30, 75, 120]
print(pm2_5_air_classify(concentrations))