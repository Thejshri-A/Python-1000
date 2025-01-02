def renewable_energy_portfolio_share(sources):
    total_energy = sum(sources.values())
    shares = {k: (v/total_energy)*100 for k,v in sources.items()}
    return {k: f"{v:.1f}" for k,v in shares.items()}

sources = {'solar': 200, 'wind': 150, 'hydro': 300}
print(renewable_energy_portfolio_share(sources))