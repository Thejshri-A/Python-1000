def title_to_num(column_title):
    result = 0
    for char in column_title:
        result = result*26 + (ord(char)-ord('A') + 1)
        
    return result

column_title = 'ZY'
print(title_to_num(column_title))