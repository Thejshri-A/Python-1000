def classify_sand(sand = 70, silt = 20, clay = 10):
    if sand>=70:
        return "Sand"
    elif 40<silt+clay<60:
        return "Loam"
    elif clay>40:
        return "Clay"

print(classify_sand())