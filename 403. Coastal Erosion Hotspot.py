def coastal_erosion_hotspot(shoreline_positions, threshold):
    shore_rate = [shoreline_positions[i-1] - pos for i,pos in enumerate(shoreline_positions[1:],1)]
    return sum(rate>threshold for rate in shore_rate)

shoreline_positions = [100, 90, 85, 75]
threshold = 5
print(coastal_erosion_hotspot(shoreline_positions, threshold))  # Output: 2