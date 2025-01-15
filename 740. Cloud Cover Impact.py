def cloud_cover_impact(baseline = 1000, cloud_cover = 0.2):
    return baseline*(1-cloud_cover)

print(cloud_cover_impact())