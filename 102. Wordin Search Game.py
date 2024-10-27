def exist(board, word):
    def dfs(i, j, word):
        if not word:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'
        
        res = (dfs(i-1, j, word[1:]) or dfs(i+1, j, word[1:]) or dfs(i, j-1, word[1:]) or dfs(i, j+1, word[1:]))
        board[i][j] = temp
        return res
    
    for i in range(len(word)):
        for j in range(len(word[0])):
            if dfs(i, j, word):
                return True
            
    return False

board = [["A", "P", "P", "I"],
         ["X", "K", "L", "O"],
         ["K", "M", "E", "S"],
         ["B", "A", "N", "A"]]
word=["A", "P", "P", "L", "E", "S"]
print(exist(board, word))