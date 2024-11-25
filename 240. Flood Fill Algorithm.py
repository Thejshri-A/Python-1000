def flood_fill_algorithm(image, sr, sc, new_color):
    original_color=image[sr][sc]
    
    if original_color==new_color:
        return image
    
    def dfs(r,c):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]!=original_color:
            return 
        image[r][c]=new_color
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        
        
    dfs(sr, sc)
    return image

# Example Usage
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc, new_color = 1, 1, 2
print(flood_fill_algorithm(image, sr, sc, new_color))