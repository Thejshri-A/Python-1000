def groundwater_overdraft(initial_groundwater = 500, recharge = [20, 25], withdrawals = [30, 40]):
    groundwater=[initial_groundwater]
    for i in range(len(recharge)):
        groundwater.append(groundwater[-1]+recharge[i]-withdrawals[i])
    return groundwater

print(groundwater_overdraft())