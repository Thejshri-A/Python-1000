def land_use_percentage(forest, agriculture, urban):
    total=forest+agriculture+urban
    forest_percent=(forest/total)*100
    agriculture_percent=(agriculture/total)*100
    urban_percent=(urban/total)*100
    return [f"Forest : {forest_percent}%",f"Agriculture : {agriculture_percent}%", f"Urban : {urban_percent}%"]

forest = 300
agriculture = 500
urban = 200
print(land_use_percentage(forest, agriculture, urban))