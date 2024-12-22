def land_classify(elevation):
    classify=[]
    for e in elevation:
        if e<500:
            classify.append("Lowland")
        else:
            classify.append("Highland")
    return classify

elevation = [200, 750, 400]
print(land_classify(elevation))