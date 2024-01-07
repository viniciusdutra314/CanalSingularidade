from manim import *
def funcao(t):
        return np.array((np.sin(2 * t), np.sin(3 * t), 0))
class PlotParametricFunction(Scene):
    def construct(self):
        func = ParametricFunction(funcao, t_range = np.array([0, TAU]), fill_opacity=0).set_color(RED)
        self.play(Write(func.scale(3)))