def glacier_retreat_trends(glacier):
    if all(glacier[i]>glacier[i+1] for i in range(len(glacier)-1)):
        return "Accelerating"
    elif all(glacier[i]<glacier[i+1] for i in range(len(glacier)-1)):
        return "Decelerating"
    else:
        return "Steady"
    
glacier=[1000, 950, 990]
print(glacier_retreat_trends(glacier))