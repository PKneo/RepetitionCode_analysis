import itertools
import numpy as np
import matplotlib.pyplot as plt

# Define original codeword mapping
bit_to_codeword = {
    '00': 'AAA',
    '01': 'CCC',
    '10': 'GGG',
    '11': 'TTT'
}
codeword_to_bit = {v: k for k, v in bit_to_codeword.items()}

nucleotides = ['A', 'C', 'G', 'T']

# Likelihood function
def likelihood(R, W, p):
    prob = 1.0
    for r, w in zip(R, W):
        if r == w:
            prob *= p
        else:
            prob *= (1 - p) / 3
    return prob

# Simulate decoding over a range of p values
p_values = np.linspace(0.25, 1.0, 100)  # p must be > 0.25 to make same-nucleotide more likely than random
error_rates = []

# Generate all 3-nucleotide combinations (64 total)
all_triplets = [''.join(t) for t in itertools.product(nucleotides, repeat=3)]

for p in p_values:
    decoding_table = {}

    # Build decoding table for this p
    for received in all_triplets:
        max_prob = -1
        most_likely_codeword = None

        for codeword in codeword_to_bit:
            prob = likelihood(received, codeword, p)
            if prob > max_prob:
                max_prob = prob
                most_likely_codeword = codeword

        decoding_table[received] = codeword_to_bit[most_likely_codeword]

    # Now simulate all 4 original codewords with noise to calculate expected error rate
    total_cases = 0
    total_errors = 0

    for original_bits, original_codeword in bit_to_codeword.items():
        for received in all_triplets:
            # Probability this original codeword becomes this received string
            prob = likelihood(received, original_codeword, p)
            decoded_bits = decoding_table[received]
            total_cases += prob
            if decoded_bits != original_bits:
                total_errors += prob

    error_rate = total_errors / total_cases
    error_rates.append(error_rate)

# Plot the error rate vs p
plt.figure(figsize=(10, 6))
plt.plot(p_values, error_rates, label="Decoding Error Rate")
plt.xlabel("Correct nucleotide probability (p)")
plt.ylabel("Decoding Error Rate")
plt.title("Decoding Error Rate vs Substitution Probability")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()