import numpy as np

# Define a vector
v = np.array([1, 0])

# Define the angle of rotation in radians
theta = np.pi/4

# Compute the rotated vector using Euler's formula
rotated_v = np.exp(1j*theta) * v

# Print the original and rotated vectors
print(f'Original vector: {v}')
print(f'Rotated vector: {rotated_v}')