from manim import *
import numpy as np
import sympy as sp
from sympy.abc import x

def taylor_series(function: callable, x0: float, degree: int):
    taylor = sp.series(function, x, x0=x0, n=degree+1).removeO().evalf()
    taylor_poly=sp.Poly(taylor,x)
    return np.polynomial.Polynomial(taylor_poly.all_coeffs()[::-1])
def reduce_precision(polynomial : np.polynomial.Polynomial,
                    precision : int)->np.polynomial.Polynomial:
    new_coeffs=[round(coeff,precision) for coeff in polynomial.coef]
    return np.polynomial.Polynomial(new_coeffs)


class TaylorSeriesVisualization(Scene):
    def construct(self):
        function = sp.tan(x)
        x0 = 0.5
        max_degree = 10
        x_min=-0.9*np.pi/2;x_max=0.9*np.pi/2
        y_min=-3;y_max=3
        axes = Axes(
            x_range=[x_min, x_max],
            y_range=[y_min,y_max],        
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label=str(function))
        
        self.play(Create(axes), Write(axes_labels))



        original_function = axes.plot(
            sp.lambdify(x,function,"numpy"),
            color=RED,
            x_range=[x_min,x_max]
        )
        self.play(Create(original_function))
        taylor_poly = taylor_series(function, x0, 1)

        taylor_function = axes.plot(
                lambda t: taylor_poly(t),
                color=GREEN,
                x_range=[x_min, x_max]
            )
        taylor_label = Text(f"{str(reduce_precision(taylor_poly,3))}").to_corner()
        self.play(Create(taylor_function), Write(taylor_label))
        for degree in range(3, max_degree + 1,2):
            new_taylor_poly = taylor_series(function, x0, degree)
            new_taylor_function = axes.plot(
                lambda t: new_taylor_poly(t),
                color=GREEN,
                x_range=[x_min, x_max]
            )
            new_taylor_label = Text(f"{str(reduce_precision(new_taylor_poly,3))}").to_corner()
            self.play(Transform(taylor_function,new_taylor_function), 
                     Transform(taylor_label,new_taylor_label))
            self.wait(1)
        self.wait(2)
