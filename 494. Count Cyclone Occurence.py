def count_cyclone_occurence(speeds):
    tropical=sum(68<=s<=110 for s in speeds)
    cyclone=sum(s>110 for s in speeds)
    return tropical, cyclone

speeds = [60, 100, 130, 90]
tropical_storm , cyclonic_storm = count_cyclone_occurence(speeds)
print(f"Tropical Storm : {tropical_storm}, Cyclonic: {cyclonic_storm}")