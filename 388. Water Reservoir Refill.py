def water_reservoir_refill(deficit, inflow):
    total=0
    days=0
    for val in inflow:
        total+=val
        days+=1
        
        if total>=deficit:
            return days
    return days


deficit = 1000
inflow = [50, 100, 150]
print(water_reservoir_refill(deficit, inflow))