from manim import *
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import approx_fprime

func = lambda x:np.sin(3*x)*np.exp(-x**2/30)+x/3
diff = lambda x:approx_fprime(x,func)[0]
class NewtonMethod(Scene):
    def construct(self):
        x0 = -3
        plane = NumberPlane(x_range=[-10,10,2],x_length=14,
                            y_range=[-5,5,50],y_length=8).add_coordinates()
        graph = plane.plot(func, color=RED)
        tracker1 = ValueTracker(x0) ; tracker2=ValueTracker(x0)
        vt1=lambda : tracker1.get_value() ; vt2=lambda : tracker2.get_value()
        tangent = always_redraw(lambda: plane.plot(
            lambda x: func(vt1()) + diff(vt1()) * (x -vt1())))
        ponto=always_redraw(lambda: Dot(plane.c2p(
            vt2(),func(vt2())),color=YELLOW))
        linha=always_redraw(lambda : Line(plane.c2p(vt2(),0),
                            plane.c2p(vt2(), func(vt2()))))
        self.add(plane, graph, tangent,ponto,linha)
        self.wait()
        while True:
            newton_step = func(x0) / diff(x0)
            x0 -= newton_step
            self.play(tracker2.animate.set_value(x0),run_time=2)
            self.play(tracker1.animate.set_value(x0),run_time=2)
            self.wait()
            if abs(newton_step) < 1e-6:break
