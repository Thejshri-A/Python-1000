def average_vegetation(coverage):
    return sum(coverage)/len(coverage)
coverage = [50, 60, 70, 80]
print(average_vegetation(coverage), "%")