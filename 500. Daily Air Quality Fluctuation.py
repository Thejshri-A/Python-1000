def daily_air_quality(air_val):
    max_diff=0
    day=-1
    for i in range(len(air_val)-1):
        
        curr_diff=max(max_diff, air_val[i+1]-air_val[i])
        if curr_diff>max_diff:
            max_diff=curr_diff
            day=i
    return day+1

air_val = [50, 55, 70, 60]   
print(daily_air_quality(air_val))