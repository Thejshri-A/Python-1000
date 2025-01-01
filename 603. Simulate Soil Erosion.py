def simulate_soil_erosion(R, K, L, S, C, P):
    return R*K*L*S*C*P

R = 50
K = 0.3
L = 2
S = 1
C = 0.5
P = 0.9
print(simulate_soil_erosion(R, K, L, S, C, P))