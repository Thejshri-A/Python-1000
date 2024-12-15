def glacier_retreat_model(glaciers):
    cumulative=[glaciers[0]]
    for i in range(1, len(glaciers)):
        curr_total=glaciers[i]+cumulative[i-1]
        cumulative.append(curr_total)
    return cumulative

glaciers = [100, 150, 120]
print(glacier_retreat_model(glaciers))