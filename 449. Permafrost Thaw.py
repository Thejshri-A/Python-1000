def permafrost_thaw(temps):
    start=-1
    thaw=[]
    
    for i in range(len(temps)):
        if temps[i]>0:
            if start==-1:
                start=i
        else:
            if start!=-1 and temps[i]<0:
                thaw.append((start, i-1))
                start=-1
    if start!=-1 and len(temps)-start>2:
        thaw.append((start, len(temps)-1))
    return thaw
# Example
result = permafrost_thaw([-5, 1, 2, 3, -1])
print(result)  
    