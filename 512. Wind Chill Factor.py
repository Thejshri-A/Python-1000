def wind_chill_factor(temp, vel):
    return 13.12+0.6215*temp-11.37*(vel**0.16)+0.3965*temp*(vel**0.16)

temp=5
vel=20
print(wind_chill_factor(temp, vel))