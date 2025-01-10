def glacial_retreat(lengths = [500, 480, 460, 450]):
    if all(lengths[i]<lengths[i+1] for i in range(len(lengths)-1)):
        return "Increasing"
    elif all(lengths[i]>lengths[i+1] for i in range(len(lengths)-1)):
        return "Decreasing"
    else:
        return "Stable"

print(glacial_retreat())
    