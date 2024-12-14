def river_flow_changes(flow):
    max_change=0
    season=-1
    
    for i in range(1, len(flow)):
        change=(abs(flow[i]-flow[i-1])/flow[i-1])*100
        if change>max_change:
            max_change=change
            season=i
    return f"The maximum change occurred from the period {season}-{season+1}"

flow=[300, 500, 250, 600]
print(river_flow_changes(flow))