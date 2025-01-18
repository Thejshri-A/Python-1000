def cyclone_intensity(speeds = [80, 100, 135, 160]):
    classify=[]
    for speed in speeds:
        if 74<=speed<=95:
            classify.append("Category 1")
        elif 96<=speed<=110:
            classify.append("Category 2")
        elif 110<=speed<=129:
            classify.append("Category 3")
        elif 130<=speed<=156:
            classify.append("Category 4")
        elif speed>156:
            classify.append("Category 5")
        else:
            classify.append("No Category")
    return classify

print(cyclone_intensity())