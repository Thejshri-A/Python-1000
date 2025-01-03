def high_elevation(elevations):
    def classification(elevation):
        if elevation>2000:
            return "Higher Elevation"
        else:
            return "Lower Elevation"
    classify=[]
    for elevation in elevations:
        classify.append(classification(elevation))
    return classify

elevations = [1500, 2200, 1800, 2500]
print(high_elevation(elevations))