from manim import *
from numpy.polynomial.polynomial import Polynomial

func = lambda x:np.sin(3*x)*np.exp(-x**2/30)+x**2/3

class NewtonMethod(Scene):
    def construct(self):
        x0 = -1
        x1=3
        plane = NumberPlane(x_range=[-10,10,2],x_length=14,
                            y_range=[-5,5,50],y_length=8).add_coordinates()
        graph = plane.plot(func, color=RED)
        tracker1 = ValueTracker(x0) ; tracker2=ValueTracker(x1)
        vt1=lambda : tracker1.get_value() ; vt2=lambda : tracker2.get_value()
        ponto1=always_redraw(lambda: Dot(plane.c2p(
            vt1(),func(vt1())),color=YELLOW))
        linha1=always_redraw(lambda : Line(plane.c2p(vt1(),0),
                            plane.c2p(vt1(), func(vt1()))))
        ponto2=always_redraw(lambda: Dot(plane.c2p(
            vt2(),func(vt2())),color=GREEN))
        linha2=always_redraw(lambda : Line(plane.c2p(vt2(),0),
                            plane.c2p(vt2(), func(vt2()))))
        reta_secante=always_redraw(lambda :Line(ponto1.copy().shift((ponto1-ponto2)*5),
                                                ponto2.copy().shift((ponto1-ponto2)*5)))
        self.add(plane, graph,ponto1,ponto2,linha1,linha2,reta_secante)
        self.wait()
        while True:
            secant_step=func(x1)*(x1-x0)/(func(x1)-func(x0))
            x2=x1-secant_step
            x0,x1=x1,x2
            self.play(tracker2.animate.set_value(x1),tracker1.animate.set_value(x0),run_time=2)
            self.wait()
            if abs(secant_step) < 1e-6:break
