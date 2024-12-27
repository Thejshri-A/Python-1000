def classify_river_flow(flows):
    classify=[]
    for flow in flows:
        if flow<50:
            classify.append("Low")
        elif 50<=flow<=100:
            classify.append("Moderate")
        else:
            classify.append("High")
    return classify

flows = [45, 70, 120]
print(classify_river_flow(flows))