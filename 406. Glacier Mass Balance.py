def glacier_mass_balance(accumulation, ablation):
    net_values= [ac-ab for ac, ab in zip(accumulation,ablation)]
    return sum(net_values), net_values

accumulation=[10, 20, 30]
ablation = [5, 15, 25]
sum_netvalues, netvalues=glacier_mass_balance(accumulation, ablation)
print("Total Glacier Mass : ", sum_netvalues, "\n Net Values : ", netvalues)