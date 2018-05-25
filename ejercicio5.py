# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sigma, beta, rho = 10, 2.67, 28.0
t,x,y,z,t_final = 0, 0.0, 0.0, 0.0, 5.0

def dxdt(x,y,z):
    return sigma*(y-x)

def dydt(x,y,z):
    return rho*x-y-x*z

def dzdt(x,y,z):
    return -beta*z+x+y

xs,ys,zs = [],[],[]
dt = 0.001
while t<t_final:
    xs.append(x)
    ys.append(y)
    zs.append(z)
    dz = dzdt(x,y,z)
    dy = dydt(x,y,z)
    dx = dxdt(x,y,z)
    z = z + dt*dz
    y = y + dt*dy
    x = x + dt*dx
    t += dt

plt.figure()
plt.plot(xs,ys)
plt.savefig('xy.png')

plt.figure()
plt.plot(xs,zs)
plt.savefig('xz.png')






