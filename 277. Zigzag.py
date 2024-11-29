def zigzag(s, rows):
    if rows==0 or rows>=len(s):
        return s
    index, step=0, 1
    result=[""]*rows
    for char in s:
        result[index]+=char
        if index==0:
            step=1
        elif index==rows-1:
            step=-1
        index+=step
    return "".join(result)

print(zigzag("PAYPALISHIRING", 3))