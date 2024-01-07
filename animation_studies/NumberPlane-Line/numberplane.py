from manim import *


class plano(Scene):
    def construct(self):
        numberplane=NumberPlane()
        vetor1=Vector([2,-1])
        vetor2=Vector([1,2],color=YELLOW)
        label1=vetor1.coordinate_label()
        label2=vetor2.coordinate_label(color=YELLOW)
        self.add(numberplane)
        self.play(Write(vetor1),FadeIn(label1))
        self.play(Transform(vetor1,vetor2),Transform(label1,label2))