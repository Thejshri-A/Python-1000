def glacier_retreat(initial_length = 3000, retreat_rate = 50, decades = 4):
    length=[initial_length]
    for i in range(decades):
        length.append(length[-1]-retreat_rate)
    return length
print(glacier_retreat())