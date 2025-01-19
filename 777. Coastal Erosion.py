def coastal_erosion(loss = [5, 6, 8], deposition = [3, 2, 4]):
    return [l-d for l,d in zip(loss,deposition)]

print(coastal_erosion())