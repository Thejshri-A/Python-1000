def drought_risk(spi = [-2.5, -1.7, -1.2]):
    classify=[]
    for val in spi:
        if val<-2.0:
            classify.append("Severe")
        elif -2.0<val<-1.5:
            classify.append("Moderate")
        elif -1.5<val<-1:
            classify.append("Mild")
    return classify

print(drought_risk())