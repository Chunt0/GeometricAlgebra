import plot

if __name__ == '__main__':
    import numpy as np
    from clifford.tools.g3 import euc_mv_to_np
    import clifford as cf
    
    # Create a 3D geometric algebra space
    layout, blades = cf.Cl(2)
    
    # Define the basis vectors
    e1 = blades['e1']
    e2 = blades['e2']
    e12 = blades['e12']
        
    x0, y0 = 1, 0  # Original vector coordinates
    
    # Build my rotator
    R = np.exp((np.pi/12)*e12)

    # Define my original 2d vector
    x = x0*e1 + y0*e2    
    
    # Rotate my vector x
    x_rot = ~R*x*R    

    # Convert x and x_rot into np.array in order to plot
    x_np = euc_mv_to_np(x)
    x_rot_np = euc_mv_to_np(x_rot)

    A = 3*e1+4*e2
    B = e1
    cos_theta = np.arccos(abs((A|B)(0)/(abs(A)*abs(B))))

    print(A)
    print(A.inv()*A)

    # Create the plotter and plot the vectors
    plot = plot.VectorPlotter([-2,2])
    #plot.plot(x_np, x_rot_np)