def river_water_flow(initial, losses_per_segment):
    flow=[initial]
    for i in range(len(losses_per_segment)):
        flow.append(flow[-1]-losses_per_segment[i])
    return flow

initial = 500
losses_per_segment = [20, 30, 50]
print(river_water_flow(initial, losses_per_segment))