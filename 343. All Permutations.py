from itertools import permutations

def all_permutations(string):
    
    return ["".join(p) for p in permutations(string)]

string="abc"
print(all_permutations(string))