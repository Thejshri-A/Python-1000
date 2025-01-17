def biodiversity(initial_species = 500, rate = 10, years = 5):
    species=[initial_species]
    for i in range(years):
        species.append(species[-1]-rate)
    return species

print(biodiversity())