def forest_cover_change(growth = [100, 110, 120], loss = [50, 60, 70]):
    return [g-l for g,l in zip(growth, loss)]

print(forest_cover_change())