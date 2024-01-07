from numpy.polynomial import Polynomial

import numpy as np
import matplotlib.pyplot as plt

def newton(x0, func, grad,expected_roots, epsilon=1e-3, max_iter=100):    
    iterations = 0
    while iterations < max_iter:
        newton_step=func(x0) / grad(x0)
        iterations += 1
        if abs(newton_step) < epsilon: break
        x0 = x0 -newton_step
    color=min(expected_roots,key=lambda root: abs(root-complex(x0)))
    return color
xmin, xmax=-1,1
ymin, ymax=-1,1
Resolution=200
polynomial = Polynomial([-1,0,0,0,1]) #-1 +0x +0x^2 +x^3
derivative = polynomial.deriv()
roots=polynomial.roots()
X, Y=np.meshgrid(np.linspace(xmin,xmax,Resolution),np.linspace(ymin,ymax,Resolution))
complex_points=X+1j*Y
converged = np.vectorize(newton)(x0=complex_points, func=polynomial, grad=derivative,expected_roots=roots)
plt.imshow(np.imag(converged))
plt.title('f(z)='+str(polynomial).replace("x","z"))
plt.savefig("Newton_fractal.png",dpi=1200)