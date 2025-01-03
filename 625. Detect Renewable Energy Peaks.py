def detect_renewable_energy_peaks(generation):
    return generation.index(max(generation))+1

generation = [100, 200, 180, 220, 90]
print(detect_renewable_energy_peaks(generation))