def animal_migration_patterns(matrix):
    transitions = [[round(val,2) for val in row] for row in matrix]
    
    return f"Analysed: {transitions}"

matrix = [[0.1, 0.9], [0.3, 0.7]]
print(animal_migration_patterns(matrix))