def aridity_zone(ai = [0.03, 0.15, 0.35, 0.6]):
    classify=[]
    for val in ai:
        if val<0.05:
            classify.append("Hyper Arid")
        elif val<0.2:
            classify.append("Arid")
        elif val<0.5:
            classify.append("Semi Arid")
        else:
            classify.append("Humid")
    return classify

print(aridity_zone())