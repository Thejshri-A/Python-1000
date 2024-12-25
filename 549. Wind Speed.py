def wind_speed(winds):
    classify=[]
    for wind in winds:
        if wind<5:
            classify.append("Calm")
        elif wind<15:
            classify.append("Moderate")
        else:
            classify.append("Strong")
    return classify

winds = [3, 8, 20]
print(wind_speed(winds))