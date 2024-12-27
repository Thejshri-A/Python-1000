def soil_moisture_index(theta, theta_min, theta_max):
    return (theta-theta_min)/(theta_max-theta_min)

theta = 0.25
theta_min = 0.1
theta_max = 0.5
print(soil_moisture_index(theta, theta_min, theta_max))