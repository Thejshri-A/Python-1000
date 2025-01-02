def carbon_sequestration(tree_area, growth_rate, carbon_factor):
    return tree_area*growth_rate*carbon_factor

tree_area = 10
growth_rate = 0.5
carbon_factor = 1.2
print(carbon_sequestration(tree_area, growth_rate, carbon_factor))