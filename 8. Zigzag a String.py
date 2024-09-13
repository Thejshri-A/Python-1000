def convert(s, no_of_rows):
    if no_of_rows == 1:
        return s
    rows = ['']*min(len(s), no_of_rows)
    curr_row, going_down = 0, False
    for char in s:
        rows[curr_row] += char
        if curr_row==0 or curr_row==no_of_rows-1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
    
    return ''.join(rows)


s="PAYPALISHIRING"
print(convert(s,3))
        