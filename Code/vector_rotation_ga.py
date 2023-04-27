import clifford as cf
from clifford.tools.g3 import euc_mv_to_np
import matplotlib.pyplot as plt
import numpy as np

# Create a 3D geometric algebra space
layout, blades = cf.Cl(3)

# Define the basis vectors
e1 = blades['e1']
e2 = blades['e2']
e3 = blades['e3']

x0, y0, z0 = 1,0,0 # Original vector coordinates
x1, y1, z1 = 1,0,0 # v1 coordinates
x2, y2, z2 = .5,np.sqrt(3)/2,0 # v2 coordinates

# Define my original 2d vector
x = x0*e1+y0*e2+z0*e3 

# Define the two vectors that I will use to rotate x by the angle between
v1 = (x1*e1 + y1*e2 + z1*e3)*(1/(np.sqrt(x1**2+y1**2+z1**2))) 
v2 = (x2*e1 + y2*e2 + z2*e3)*(1/(np.sqrt(x2**2+y2**2+z2**2))) 

# Find the angle between these two vectors
# Gotta convert the vector to a np.array, the function angle_between_vectors doesn't seem to work...
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
xlim = 5
ylim = 5
ax.set_xlim([-1*xlim, xlim])
ax.set_ylim([-1*ylim, ylim])

# Set the aspect ratio to make the plot square
ax.set_aspect('equal')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('GA Vector Plot')

# Add text annotation for the angle between the vectors
ax.text(0.5, 2.5, f'Angle: {theta:.2f} degrees', fontsize=12)

# Show the plot
plt.show()