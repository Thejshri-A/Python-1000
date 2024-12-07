def predict_tree_growth(initial_height, growth_rate, years):
    return initial_height+(growth_rate*years)

# Example
initial_height = 2
growth_rate = 0.5
years = 10
print(predict_tree_growth(initial_height, growth_rate, years))  # Output: 7
