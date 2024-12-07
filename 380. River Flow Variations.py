def river_flow_variations(discharge):
    
    peak=max(discharge)
    peak_90 = 0.9*peak
    count=0
    for val in discharge:
        if val>=peak_90:
            count+=1
    return peak, count
discharge = [50, 200, 300, 250, 100]
peak, count=river_flow_variations(discharge)
print(f'Peak : {peak}, Number of Days Exceeding 90% of Peak : {count}')