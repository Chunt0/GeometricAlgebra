import clifford as cf
from clifford.tools.g3 import euc_mv_to_np
import matplotlib.pyplot as plt
import numpy as np

# Create a 2D geometric algebra space
layout, blades = cf.Cl(3)

# Define the basis vectors
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']
e12 = blades['e12']

# Define my original 2d vector
x = e1

# Define the two vectors that I will use to rotate x by the angle between
# Current angle = pi/4
v1 = 1*e1 + 0*e2 + 0*e3 # [1,0,0]
v2 = 1*e1 + 1*e2 + 0*e3 # [1,1,0]

# Find the angle between these two vectors
# Gotta convert the vector to a np.array, the function angle_between_vectors
# Doesn't seem to work...
v1_np = euc_mv_to_np(v1)
v2_np = euc_mv_to_np(v2)
cos_theta = np.dot(v1_np, v2_np) / (np.linalg.norm(v1_np) * np.linalg.norm(v2_np))
theta = np.arccos(cos_theta)

# Rotate my vector x
x_rot = v1*v2*x
print(f"Rotation Angle: {theta*(180/np.pi)}")
print(f"Original Vector: {x}")
print(f"Rotated vector: {x_rot}")

# Convert x and x_rot into np.array in order to plot
x_np = euc_mv_to_np(x)
x_rot_np = euc_mv_to_np(x_rot)

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the vectors
ax.quiver(0, 0, x_np[0], x_np[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, x_rot_np[0], x_rot_np[1], angles='xy', scale_units='xy', scale=1, color='b')

# Calculate the angle between the original vector and the rotated one
cos_theta = np.dot(x_np, x_rot_np) / (np.linalg.norm(x_np) * np.linalg.norm(x_rot_np))
theta = np.arccos(cos_theta) * 180 / np.pi

# Set the limits of the plot
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('GA Vector Plot')

# Add text annotation for the angle between the vectors
ax.text(0.5, 2.5, f'Angle: {theta:.2f} degrees', fontsize=12)

# Show the plot
plt.show()