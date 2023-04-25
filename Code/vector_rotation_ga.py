import clifford as cf
import matplotlib.pyplot as plt
import numpy as np

# Creat a 2D geometric algebra space
layout, blades = cf.C1(2)

# Define the basis vectors
e1 = blades['e1']
e2 = blades['e2']
e12 = blades['e12']

# My original 2d vector
x = e1

# My two vectors that I will use to rotate x by the angle between
# Current angle = pi/4
v1 = 1*e1 # [1,0]
v2 = 1*e1 + 1*e2 # [1,1]

# Rotate my vector x
x_rot = v1*v2*x
print(x_rot)
if np.linalg.norm(x_rot[0]) == 0: 
    x_rot = np.array([np.real(x_rot[1]), np.imag(x_rot[1])])
else:
    x_rot = np.array([np.real(x_rot[0]), np.imag(x_rot[0])])
print(x_rot)

# Show the plot
plt.show()# Extract the x and y components of the vectors
x = [x(e1), x_rot(e1)]
y = [x(e2), x_rot(e2)]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the vectors
ax.quiver([0, 0], [0, 0], x, y, angles='xy', scale_units='xy', scale=1, color=['r', 'b'])

# Set the limits of the plot
ax.set_xlim([-3, 3])
ax.set_ylim([-1, 4])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Vector Plot')

# Show the plot
plt.show()