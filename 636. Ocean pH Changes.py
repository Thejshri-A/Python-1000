def ocean_pH_changes(pH_levels = [7.8, 7.4, 7.6, 7.3]):
    changes=[]
    for i, pH in enumerate((pH_levels)):
        if pH<7.5:
            changes.append(i+1)
    return changes

print(ocean_pH_changes())