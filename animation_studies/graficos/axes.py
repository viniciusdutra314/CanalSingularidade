from manim import *

class axesExample(Scene):
    def construct(self):
        ax=Axes(x_range=[0,5],y_range=[0,30,10],
                tips=False,axis_config={'include_numbers':True})
        graph=ax.plot(lambda x: np.power(2,x),color=RED)
        self.play(Write(ax))
        self.play(Write(graph))