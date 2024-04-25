from itertools import permutations

def generate_permutations(word):
    # Generate all permutations of the letters in the word
    perms = permutations(word)
    
    # Convert permutations to a list of strings
    perm_strings = [''.join(perm) for perm in perms]
    
    return [perm for perm in perm_strings]

# Example usage:
word = "abcdbhdgsft"
permutations = generate_permutations(word)
print(permutations)
