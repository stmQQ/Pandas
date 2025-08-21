import itertools

#Task 1: Lock combinations

def lock_combinations():
    all_combinations = itertools.permutations(range(10), 4)
    suitable_combinations = filter(lambda x: x[0] % 2 == 0 and x[1] % 2 == 1, all_combinations)

    return list(suitable_combinations)


#Task 2: Text analysis

def analyze_text(text):
    all_pairs = itertools.product(text)
    print(list(all_pairs))


analyze_text('Data science requires statistics and programming. Machine learning uses algorithms and models. Neural networks have layers and neurons. Gradient descent optimizes loss functions. Training data must be clean and representative. Validation helps prevent overfitting.')
