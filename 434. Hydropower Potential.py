def hydropower_potential(height,flow_rate,efficiency=0.8, density=1000, gravity=9.8 ):
    return round(efficiency*density*gravity*height*flow_rate/100,2)

height = 50
flow_rate = 10
print("Hydropower Potential : ", hydropower_potential(height, flow_rate), " W")