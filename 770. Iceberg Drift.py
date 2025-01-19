import math
def iceberg_drift(speed = 10, angle = 45):
    dx=speed*math.cos(math.radians(angle))
    dy=speed*math.sin(math.radians(angle))
    return dx,dy

print(iceberg_drift())