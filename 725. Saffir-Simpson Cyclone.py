def saffir_simpson_cyclone(wind_speeds = [80, 100, 120]):
    classify=[]
    for wind in wind_speeds:
        if 74<=wind<95:
            classify.append("Category 1")
        elif 95<=wind<=110:
            classify.append("Category 2")
        elif 110<wind:
            classify.append("Category 3")
    return classify


print(saffir_simpson_cyclone())