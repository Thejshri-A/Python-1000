def max_area_of_water(height):
    left, right=0, len(height)-1
    maxArea=0
    while left<right:
        maxArea=max(maxArea, min(height[left], height[right])*(right-left))
        
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxArea

# Example Usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area_of_water(height))  # Output: 49









    