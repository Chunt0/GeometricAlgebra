import matplotlib.pyplot as plt
import numpy as np

class VectorPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        
        # Set the limits of the plot
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        
        # Set the aspect ratio to make the plot square
        self.ax.set_aspect('equal')
        
        # Add labels and title
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('GA Vector Plot')
    
    def plot(self, x_np, x_rot_np):
        # Plot the vectors
        self.ax.quiver(0, 0, x_np[0], x_np[1], angles='xy', scale_units='xy', scale=1, color='r')
        self.ax.quiver(0, 0, x_rot_np[0], x_rot_np[1], angles='xy', scale_units='xy', scale=1, color='b')
        
        # Calculate the angle between the original vector and the rotated one
        cos_theta = np.dot(x_np, x_rot_np) / (np.linalg.norm(x_np) * np.linalg.norm(x_rot_np))
        theta = np.arccos(cos_theta) * 180 / np.pi
        
        # Add text annotation for the angle between the vectors
        self.ax.text(0.5, 2.5, f'Angle: {theta:.2f} degrees', fontsize=12)
        
        # Show the plot
        plt.show()
