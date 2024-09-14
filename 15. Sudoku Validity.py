def check_sudoku_validity(board):
    rows, cols, boxes = {}, {}, {}
    for r in range(9):
        for c in range(9):
            box_index= (r//3)*3 + (c//3)
            if board[r][c]==".":
                continue
            
            if (board[r][c] in rows.get(r, set()) or 
                board[r][c] in cols.get(c, set()) or
                board[r][c] in boxes.get(box_index, set())):
                return False
            
            rows.setdefault(r, set()).add(board[r][c])
            cols.setdefault(c, set()). add(board[r][c])
            boxes.setdefault(box_index, set()).add(board[r][c])
            
    return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(check_sudoku_validity(board))