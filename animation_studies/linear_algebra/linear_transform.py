from manim import *



class LinearTransform(LinearTransformationScene):
    def construct(self):
        matrix=[[0,1],[1,0]]
        self.apply_matrix(matrix)
        self.wait(2)