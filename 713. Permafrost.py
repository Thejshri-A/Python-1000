def permafrost(initial_thaw = 0, rate = 0.5, years = 5):
    thaw=[initial_thaw]
    for i in range(years):
        thaw.append(thaw[-1]+rate)
    return thaw

print(permafrost())