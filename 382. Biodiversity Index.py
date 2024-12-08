def calculate_biodiversity_index(species_counts):
    
    total= sum(species_counts)
    no_of_species=len(species_counts)
    return no_of_species/total
    
species_counts = [50, 30, 20, 100]
print(calculate_biodiversity_index(species_counts))