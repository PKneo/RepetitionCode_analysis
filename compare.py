import numpy as np
import matplotlib.pyplot as plt

# Define functions
def f(x):
    return 3 * x**2 - 2 * x**3

def g(x):
    return x

# Create x values
x = np.linspace(0, 1, 300)
y_f = f(x)
y_g = g(x)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y_f, label=r'Triple-nucleotide code $P_e$', color='blue', linewidth=2)
plt.plot(x, y_g, label=r'Uncoded (no redundancy)', linestyle='--', color='red', linewidth=2)

# Highlight intersection point at x = 0.5
plt.axvline(x=0.5, color='gray', linestyle=':', linewidth=1)
plt.plot(0.5, f(0.5), 'ko')  # intersection point

# Labels and title
plt.xlabel(r'Substitution probability $q$', fontsize=12)
plt.ylabel(r'Decoding error probability $P_e$', fontsize=12)
plt.title('Decoding Error Probability vs Substitution Probability', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True)
plt.tight_layout()
plt.show()
