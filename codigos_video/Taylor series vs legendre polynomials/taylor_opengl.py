from manim import *
from manim.opengl import *
import numpy as np
import sympy as sp
from sympy.abc import x

def taylor_series(function: callable, x0: float, degree: int):
    taylor = sp.series(function, x, x0=x0, n=degree+1).removeO().evalf()
    taylor_poly=sp.Poly(taylor,x)
    return np.polynomial.Polynomial(taylor_poly.all_coeffs()[::-1])



class TaylorSeriesVisualization(Scene):
    def construct(self):
        self.function = sp.exp(x)
        self.x0 = 0.5
        self.x_min=-0.9*np.pi/2;self.x_max=0.9*np.pi/2
        y_min=-3;y_max=3
        self.axes = Axes(
            x_range=[self.x_min, self.x_max],
            y_range=[y_min,y_max],        
            axis_config={"color": BLUE}
        )
        axes_labels = self.axes.get_axis_labels(x_label="x", y_label=str(self.function))
        
        self.play(Create(self.axes), Write(axes_labels))
        original_function = self.axes.plot(
            sp.lambdify(x,self.function,"numpy"),
            color=RED,
            x_range=[self.x_min,self.x_max]
        )
        self.play(Create(original_function))
        self.interactive_embed()
    def update_values(self,x0:float,degree:int):
        if "x0_text" in dir(self):
            self.play(FadeOut(self.x0_text,self.degree_text))
        self.x0_text=Tex(f"{x0=:.2f}").to_corner(corner=[-1,1,0])
        self.degree_text=Tex(f"N={degree}").next_to(self.x0_text,DOWN)
        self.play(FadeIn(self.x0_text,self.degree_text))
   
    def animate_taylor(self,x0:float,degree:int):
        if ("new_taylor_function" in dir(self)):
            self.play(FadeOut(self.new_taylor_function))
        self.new_taylor_poly = taylor_series(self.function, x0, degree)
        self.new_taylor_function = self.axes.plot(
            lambda t: self.new_taylor_poly(t),
            color=GREEN,
            x_range=[self.x_min, self.x_max]
        )
        self.play(FadeIn(self.new_taylor_function))
        self.update_values(x0,degree)
        
    def reduce_precision(self,polynomial : np.polynomial.Polynomial,
                    precision : int)->np.polynomial.Polynomial:
        new_coeffs=[round(coeff,precision) for coeff in polynomial.coef]
        return np.polynomial.Polynomial(new_coeffs)