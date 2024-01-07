from manim import *

class numberline(Scene):
    def construct(self):
        numberline=NumberLine(x_range=[0,1,0.1],length=10,
                    include_numbers=True,rotation=30*DEGREES)
        self.add(numberline)