def land_surface_albedo(reflectance = [0.3, 0.6, 0.1], areas = [40, 30, 30]):
    return sum(r*a for r,a in zip(reflectance, areas))/sum(areas)

print(land_surface_albedo())