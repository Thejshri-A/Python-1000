def cyclone_category(speeds):
    classify=[]
    def cyclone(speed):
        if 74<speed<95:
            return "Category 1"
        elif 95<speed<110:
            return "Category 2"
        elif speed>110:
            return "Category 3"
    for speed in speeds:
        classify.append(cyclone(speed))
    return classify

speeds = [80, 100, 120]
print(cyclone_category(speeds))