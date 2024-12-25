def albedo(reflected, incoming):
    return reflected/incoming

reflected = 300
incoming = 500
print(albedo(reflected, incoming))