def longest_below_threshold(soil_moisture, threshold):
    longest, current = 0,0
    
    for level in soil_moisture:
        if level<threshold:
            current+=1
            longest=max(longest, current)
        else:
            current=0
    
    return longest

# Example
soil_moisture = [30, 25, 20, 50, 40, 15, 10, 30]
threshold = 30
print(longest_below_threshold(soil_moisture, threshold))  # Output: 2
