import plot

if __name__ == '__main__':
    import numpy as np
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
    plot = plot.VectorPlotter([-5,5])
    plot.plot(x_np, x_rot_np)