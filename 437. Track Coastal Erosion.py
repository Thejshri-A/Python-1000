def track_coastal_erosion(distance, erosion):
    change_in_distance=0
    change_in_erosion = 0
    coastal_erosion=[]
    for i in range(1, len(distance)):
        change_in_distance = distance[i-1]-distance[i]
        change_in_erosion = erosion[i-1]-erosion[i]
        coastal_erosion.append(change_in_distance/change_in_erosion)
        
    return coastal_erosion

distance = [10, 8, 5]
erosion = [2000, 2010, 2020]

print("Coastal Erosion : ", track_coastal_erosion(distance, erosion)," km/year.")
    