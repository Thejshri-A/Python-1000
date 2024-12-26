def hottest_and_coldest(temps):
    hottest=temps.index(max(temps))
    coldest=temps.index(min(temps))
    return f"Hottest : {hottest+1}, Coldest : {coldest+1}"

temps = [20, 25, 30, 18, 27]
print(hottest_and_coldest(temps))