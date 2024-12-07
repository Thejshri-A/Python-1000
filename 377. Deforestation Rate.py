def deforestation_rate(forest_area):
    deforest=[]
    for  i in range(1,len(forest_area)):
        if forest_area[i]<forest_area[i-1]:
            percent=round(abs(((forest_area[i-1]-forest_area[i])/forest_area[i-1])*100),2)
            deforest.append(percent)
        else:
            deforest.append("None")
    return deforest

forest_area = [500, 450, 400, 370]
print(deforestation_rate(forest_area))