def evapotranspiration(precipitation, runoff):
    return precipitation-runoff

precipitation = 800
runoff = 300
print(evapotranspiration(precipitation, runoff))