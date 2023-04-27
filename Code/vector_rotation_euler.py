import clifford as cf
import matplotlib.pyplot as plt
import numpy as np

# Euler's formula to rotate a vector by theta
# There's an issue with getting a vector back with complex components
# and sometimes one or the other value in the list is 0. Anyway this tries
# to clean things up and give me a nice np.array to work with.
def eulers_rot(vec, theta):
    complex_rotation = (vec[0] + vec[1]*1j)*np.exp(1j*theta)
    vec_rot =np.array([np.real(complex_rotation), np.imag(complex_rotation)])
    return vec_rot

# My base vector that I'm going to rotate
x = np.array([1,3])

# Some vectors that I'll use to form random angles of theta
v1 = np.array([-1, 0 ])
v2 = np.array([0, -1])

# Calculate the angle between these vectors
cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
theta = np.arccos(cos_theta)
print(f"Theta: {theta*(180/np.pi)}")

# Rotate my vector x
# The product from eulers
x_rot = eulers_rot(x, theta)

# Print values
print(f"Rotation Angle: {theta*(180/np.pi)}")
print(f"Original Vector: {x}")
print(f"Rotated vector: {x_rot}")

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the vectors
ax.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, x_rot[0], x_rot[1], angles='xy', scale_units='xy', scale=1, color='b')

# Calculate the angle between the original vector and the rotated one
cos_theta = np.dot(x, x_rot) / (np.linalg.norm(x) * np.linalg.norm(x_rot))
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
ax.set_title('Vector Plot')

# Add text annotation for the angle between the vectors
ax.text(0.5, 2.5, f'Angle: {theta:.2f} degrees', fontsize=12)

# Show the plot
plt.show()