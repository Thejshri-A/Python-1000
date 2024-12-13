def coral_bleaching(temps):
    return [i+1 for i in range(len(temps)) if temps[i]>30]

temps = [28, 31, 29, 32]
print("Coral Bleacing : ", coral_bleaching(temps))