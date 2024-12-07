def glacier_retreat_rate(retreat):
    retreat_rate=[]
    
    for i in range(1,len(retreat)):
        percent_val=((retreat[i-1]-retreat[i])/retreat[i-1])*100
        retreat_rate.append(percent_val)
        
    return retreat_rate
# Example
retreat = [1000, 950, 900, 850]
print(glacier_retreat_rate(retreat))  # Output: [5.0, 5.26, 5.56]