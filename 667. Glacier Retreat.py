def glacier_retreat(positions):
    return sum(positions[i]-positions[i+1] for i in range(len(positions)-1))/(len(positions)-1)

positions = [1000, 950, 900, 870]
print(glacier_retreat(positions))