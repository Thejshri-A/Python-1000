def drought_prone(rainfall = [500, 400, 600, 700], threshold = 450):
    drought=[]
    for val in rainfall:
        if val<threshold:
            drought.append(rainfall.index(val)+1)
    return drought

print(drought_prone())