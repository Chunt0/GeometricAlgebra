import clifford as cf
import matplotlib.pyplot as plt
import numpy as np

# Euler's formula to rotate a vector by theta
# There's an issue with getting a vector back with complex components
# and sometimes one or the other value in the list is 0. Anyway this tries
# to clean things up and give me a nice np.array to work with.
def eulers_rot(vec, theta):
    vec_mag = np.linalg.norm(vec) # For some reason I need to rescale the rotated vector?
    vec_rot = vec*np.exp(1j*theta)
    print(vec_rot)
    if np.linalg.norm(vec_rot[0]) == 0: 
        vec_rot = np.array([np.real(vec_rot[1]), np.imag(vec_rot[1])])
    else:
        vec_rot = np.array([np.real(vec_rot[0]), np.imag(vec_rot[0])])
    return vec_rot

# My base vector that I'm going to rotate
x = np.array([1,4])

# Some vectors that I'll use to form random angles of theta
v1 = np.array([-1, -1])
v2 = np.array([5, -2])

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
ax.set_xlim([-3, 3])
ax.set_ylim([-1, 4])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Vector Plot')

# Add text annotation for the angle between the vectors
ax.text(0.5, 2.5, f'Angle: {theta:.2f} degrees', fontsize=12)

# Show the plot
plt.show()