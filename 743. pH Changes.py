def ph_changes(initial_pH = 8.2, delta = 0.1, years = 5):
    pH=[initial_pH]
    for i in range(years):
        pH.append(pH[-1]-delta)
        
    return pH

print(ph_changes())