def habitat_sustainability_index(weights, scores):
    return sum(w*s for w,s in zip(weights, scores))

weights = [0.3, 0.5]
scores = [0.8, 0.9]
print(habitat_sustainability_index(weights, scores))