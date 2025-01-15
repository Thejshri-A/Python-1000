def sediment_transport(flow = [500, 600, 550], concentration = 0.3):
    return [f*concentration for f in flow]

print(sediment_transport())