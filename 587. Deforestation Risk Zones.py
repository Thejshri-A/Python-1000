def deforestation_risk_zones(forest_loss):
    classify=[]
    for val in forest_loss:
        if val<10:
            classify.append("Low")
        elif val<30:
            classify.append("Moderate")
        else:
            classify.append("High")
    return classify
forest_loss = [5, 15, 40]
print(deforestation_risk_zones(forest_loss))
    