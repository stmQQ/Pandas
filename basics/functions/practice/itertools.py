import itertools
import re
import sympy

# Task 1: Lock combinations

def lock_combinations():
    all_combinations = itertools.permutations(range(10), 4)
    suitable_combinations = filter(lambda x: x[0] % 2 == 0 and x[1] % 2 == 1, all_combinations)

    return list(suitable_combinations)


# Task 2: Text analysis

def analyze_text(text: str):
    all_words = re.findall(r'\w+', text)
    all_pairs = itertools.pairwise(all_words)
    suitable_pairs = filter(lambda x: len(x[0]) == len(x[1]) and x[0].lower() != x[1].lower(), all_pairs)
    return list(suitable_pairs)

    
# Task 3: 

def dice_combinations(dice_n: int, dice_edges: int):
    all_combinations = itertools.combinations(range(1, dice_edges + 1), dice_n)
    good_combinations = []
    for comb in all_combinations:
        if len(set(comb)) == len(comb) and sympy.isprime(sum(comb)):
            good_combinations.append(comb)
    
    return good_combinations


print(dice_combinations(3, 6))