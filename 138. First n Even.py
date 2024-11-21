def first_n_even(n):
    n_even_arr = []
    for i in range(1, n+1):
        n_even_arr.append(i*2)
    
    return n_even_arr

n=4
print(first_n_even(n))