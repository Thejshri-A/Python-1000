def high_risk_drought_months(spi):
    return sum([1 for val in spi if val<-1.5])

spi = [-1.6, -0.5, -1.2, -1.8, -0.7, -2.0]
print(high_risk_drought_months(spi))