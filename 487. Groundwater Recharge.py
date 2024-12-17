def groundwater_recharge(infilteration, area):
    return infilteration*area

infilteration = 10
area = 100
print("Recharge Units : ", groundwater_recharge(infilteration, area), " units")