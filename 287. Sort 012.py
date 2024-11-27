def sorting(arr):
    zero=[]
    one=[]
    two=[]
    res=[]
    
    for s in arr:
        if s==0:
            res.append(s)
    for s in arr:
        if s==1:
            res.append(s)
    for s in arr:
        if s==2:
            res.append(s)
    
    return res

print(sorting([1, 2, 0, 1]))
    