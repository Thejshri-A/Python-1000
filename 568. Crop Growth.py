def crop_growth(heights):
    classify=[]
    for height in heights:
        if height<10:
            classify.append("Germination")
        elif height<50:
            classify.append("Vegetative")
        else:
            classify.append("Reproductive")
    return classify

heights = [5, 20, 60]
print(crop_growth(heights))