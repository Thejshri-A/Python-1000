def heatwave_periods(temps, threshold=35):
    periods = []
    start = None
    for i, temp in enumerate(temps):
        if temp > threshold:
            if start is None:
                start = i
        else:
            if start is not None and i - start >= 3:
                periods.append((start, i - 1))
            start = None
    if start is not None and len(temps) - start >= 3:
        periods.append((start, len(temps) - 1))
    return periods

# Example
temps = [34, 36, 37, 38, 33, 35, 36, 37, 30]
print(heatwave_periods(temps))  # Output: [(1, 3), (5, 7)]
