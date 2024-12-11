def tsunami_propagation_speed(gravitational_acc, ocean_depth):
    return [round((depth*gravitational_acc)**0.5,2) for depth in ocean_depth]

ocean_depth = [100, 500, 1000]
gravitational_acc=9.8
print(tsunami_propagation_speed(gravitational_acc, ocean_depth))