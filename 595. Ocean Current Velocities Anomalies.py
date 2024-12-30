def ocean_current_vel(velocities, threshold):
    anomalies=[]
    for vel in velocities:
        if vel<threshold:
            anomalies.append("Normal")
        else:
            anomalies.append("Anomalous")
    return anomalies

velocities = [1.5, 2.0, 3.5]
threshold = 2.5
print(ocean_current_vel(velocities, threshold))