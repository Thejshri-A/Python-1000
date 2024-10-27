def searchMatrix(mat, num):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==num:
                return True
    return False

mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num=30
print(searchMatrix(mat, num))