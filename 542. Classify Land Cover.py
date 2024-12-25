def classify_land_cover(ndvi):
    classify=[]
    for val in ndvi:
        if val<0.2:
            classify.append("Barren")
        elif val<0.5:
            classify.append("Grassland")
        else:
            classify.append("Forest")
    return classify

ndvi = [0.1, 0.3, 0.7]
print(classify_land_cover(ndvi))