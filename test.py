import clifford as cf

layout, blades = cf.Cl(3)

x = blades['e1']
y = blades['e2']
z = blades['e3']

xy = blades['e12']
yz = blades['e23']

a = (x + 2*y + 3*z)
B = (xy + yz)

print(a*B)