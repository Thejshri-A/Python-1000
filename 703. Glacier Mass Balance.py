def glacier_mass_balance(accumulation = [200, 250], ablation = [180, 300]):
    return [ac-ab for ac, ab in zip(accumulation, ablation)]

print(glacier_mass_balance())