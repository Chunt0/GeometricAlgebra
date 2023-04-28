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

# Example usage
if __name__ == '__main__':
    from clifford.tools.g3 import euc_mv_to_np
    import clifford as cf
    
    # Create a 3D geometric algebra space
    layout, blades = cf.Cl(3)
    
    # Define the basis vectors
    e1 = blades['e1']
    e2 = blades['e2']
    e3 = blades['e3']
    
    x0, y0, z0 = 1, 0, 0  # Original vector coordinates
    x1, y1, z1 = 1, 0, 0  # v1 coordinates
    x2, y2, z2 = 0.5, np.sqrt(3)/2, 0  # v2 coordinates
    
    # Define my original 2d vector
    x = x0*e1 + y0*e2 + z0*e3
    
    # Define the two vectors that I will use to rotate x by the angle between
    v1 = (x1*e1 + y1*e2 + z1*e3) * (1/(np.sqrt(x1**2 + y1**2 + z1**2)))
    v2 = (x2*e1 + y2*e2 + z2*e3) * (1/(np.sqrt(x2**2 + y2**2 + z2**2)))
    
    # Rotate my vector x
    x_rot = v1 * v2 * x
    
    # Convert x and x_rot into np.array in order to plot
    x_np = euc_mv_to_np(x)
    x_rot_np = euc_mv_to_np(x_rot)
    
    # Create the plotter and plot the vectors
    plotter = VectorPlotter()
    plotter.plot(x_np, x_rot_np)
