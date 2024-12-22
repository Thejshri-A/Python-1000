def cel_to_f(cel):
    return [c*(9/5)+32 for c in cel]

cel = [0, 25, 100]
print(cel_to_f(cel))