def hydropwer(efficiency = 0.9, density = 1000, gravity = 9.8, height = 50, flow = 10):
    return efficiency*density*gravity*height*flow

print(hydropwer())