import clifford as cf
from clifford.tools.g3 import angle_between_vectors, euc_mv_to_np

# Create a 3D geometric algebra space
layout, blades = cf.Cl(3)

# Define two conformal vectors
v1 = 1 + 2*blades['e1'] + 3*blades['e2'] + 4*blades['e3']
v2 = 2 + 3*blades['e1'] + 1*blades['e2'] - 2*blades['e3']

# Compute the angle between the vectors
v1_np = euc_mv_to_np(v1)
v2_np = euc_mv_to_np(v2)

print(v1_np)