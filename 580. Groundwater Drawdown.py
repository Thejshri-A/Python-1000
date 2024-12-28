def groundwater_drawdown(initial_level, withdrawals):
    level=[initial_level]
    for i in range(len(withdrawals)):
        level.append(level[-1]-withdrawals[i])
    return level

initial_level = 100
withdrawals = [5, 10, 7]
print(groundwater_drawdown(initial_level, withdrawals))