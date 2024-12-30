def albedo(reflected, incoming):
    return reflected/incoming

reflected = 300
incoming = 1000

print("Albedo: ", albedo(reflected, incoming))