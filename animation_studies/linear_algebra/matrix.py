from manim import *


class MatrizExemplo(Scene):
    def construct(self):
        np.random.seed(400)
        m=Matrix(np.round(np.random.random(size=(4,4)),2))
        self.add(m)
        self.wait()
        self.play(Rotate(m,angle=45*DEGREES))