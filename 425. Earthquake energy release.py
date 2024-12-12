import math

def earthquake_energy_release(magnitude):
    return [round(math.pow(10,1.5*mag+4.8),2) for mag in magnitude]

magnitude = [5, 6, 7]
print(earthquake_energy_release(magnitude))

