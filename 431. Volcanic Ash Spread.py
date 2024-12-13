def volcanic_ash_spread(speed, time, direction):
    return speed*time, direction

speed=20
time=5
direction="North"

distance, towards=volcanic_ash_spread(speed, time, direction)

print(f"The Volcanic Ash Spreads in {distance} km in {towards}wards direction")