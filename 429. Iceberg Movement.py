import math

def iceberg_movement(coordinates):
    distance=[]
    for i in range(len(coordinates)-1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        val = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
        distance.append(val)
    return distance

coordinates = [(0, 0), (3, 4), (6, 8)]
    

print("Iceberge Movement : ", iceberg_movement(coordinates))