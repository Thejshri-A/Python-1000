def urban_heat_islands(urban, rural):
    return sum(u>r+5 for u,r in zip(urban, rural))

# Example
urban = [30, 35, 40]
rural = [25, 30, 32]
print(urban_heat_islands(urban, rural))  # Output: 2