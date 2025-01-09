def coastal_erosion(areas = [1000, 990, 970, 960], threshold = 15):
    erosion=[]
    for i in range(1, len(areas)):
        if abs(areas[i]-areas[i-1]) >=15:
            erosion.append(i)
    return erosion

print(coastal_erosion())