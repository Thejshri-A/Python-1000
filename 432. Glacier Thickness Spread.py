def glacier_thickness(melting_rate, time):
    return [melting_rate*t for t in time]

melting_rate = 0.5
time = [1, 2, 3]
print("Glacier Thickness :", glacier_thickness(melting_rate, time))