def desertification_trends(rainfall):
    trends=[]
    for i in range(1, len(rainfall)):
        trend = round(((rainfall[i-1]-rainfall[i])/rainfall[i-1])*100,2)
        trends.append(trend)
        
    return trends
rainfall = [500, 450, 400, 350]
print(desertification_trends(rainfall))
    