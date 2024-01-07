from manim import *
import numpy as np

class funcao(Scene):
    def construct(self):
        func1=FunctionGraph(np.cos) 
        func2=FunctionGraph(lambda x: np.cos(2*x))
        self.play(Write(func1))
        self.play(Transform(func1,func2))