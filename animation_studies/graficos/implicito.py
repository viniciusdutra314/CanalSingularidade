from manim import *
import numpy as np

class funcao(Scene):
    def construct(self):
        func1=ImplicitFunction(lambda x,y :np.exp(y)-x**3+x+np.cos(y) -1) 
        self.play(Write(func1))
        