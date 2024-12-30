def seasonal_water_demands(usage):
    seasonal={"Winter": usage[11:]+usage[:2],
              "Spring": usage[2:5],
              "Summer":usage[5:8],
              "Autumn":usage[8:11]
        }
    winter =sum(seasonal["Winter"])
    summer =sum(seasonal["Summer"])
    return f"Winter : {winter}, Summer: {summer}"

usage = [50, 60, 70, 80, 100, 90, 60, 50, 40, 30, 20, 15]
print(seasonal_water_demands(usage))