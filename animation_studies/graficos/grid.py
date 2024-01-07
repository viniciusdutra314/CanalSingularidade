from manim import *

class grid(Scene):
    def construct(self):
        ax=Axes(x_range=[0,5],y_range=[0,30,10],
                tips=False,axis_config={'include_numbers':True})
        ax=ax.add_coordinates()
        graph=ax.plot(lambda x: np.power(2,x),color=RED)
        self.add(NumberPlane(ax.coords_to_point(0,0)))
        self.play(Write(ax))
        self.play(Write(graph))