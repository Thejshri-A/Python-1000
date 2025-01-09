def renewable_energy_potential(energy = [100, 120, 150, 80, 90, 110]):
    return f"Total: {sum(energy)}, Peak: {max(energy)}"

print(renewable_energy_potential())