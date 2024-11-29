def largest_rect_in_hist(heights):
    stack=[]
    maxArea=0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]]>h:
            height=heights[stack.pop()]
            width=i if not stack else i-stack[-1]-1
            maxArea=max(maxArea, height*width)
        stack.append(i)
    return maxArea
# Example Usage
print(largest_rect_in_hist([2, 1, 5, 6, 2, 3]))