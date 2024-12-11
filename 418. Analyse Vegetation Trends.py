def analyse_vegetation_trends(ndvi):
    monthly_trend=[((ndvi[i+1]-ndvi[i])/ndvi[i]) *100 for i in range(len(ndvi)-1)]
    annual_trend = round(sum(monthly_trend)/len(monthly_trend),2)
    return annual_trend
ndvi = [0.3, 0.35, 0.4, 0.45]
print("Annual Trend : ",analyse_vegetation_trends(ndvi), "%")