def drought_severity(spi_val):
    classify=[]
    for val in spi_val:
        if val<-1.5:
            classify.append("Severe")
        elif -1.5<=val<=-1:
            classify.append("Moderate")
        elif -1<val:
            classify.append("Normal")
        else:
            classify.append("Check")
    return classify

spi_val = [-1.6, -1.2, -0.8]
print(drought_severity(spi_val))