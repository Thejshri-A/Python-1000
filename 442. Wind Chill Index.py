def wind_chill_index_calc(temp,vel):
    wind_chill_index=13.12+0.6215*temp-11.37*(vel**0.16)+0.3965*temp*(vel**0.16)
    return wind_chill_index

temp=10
vel=20
print("Wind Chill Index : ", wind_chill_index_calc(temp, vel))