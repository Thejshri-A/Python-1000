def riverflow_dynamics(initial_flow, incoming, outgoing):
    river=[initial_flow]
    for i,o in zip(incoming,outgoing):
        river.append(river[-1]+i-o)
    return river
    
    
initial_flow = 100
incoming = [20, 30]
outgoing = [10, 40]
print(riverflow_dynamics(initial_flow, incoming, outgoing))