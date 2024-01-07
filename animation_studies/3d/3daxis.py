from manim import *


class axis3d(ThreeDScene):
    def construct(self):
        axes=ThreeDAxes()
        axes_label=axes.get_axis_labels(Tex('x'),Tex('y'),Tex('z'))
        self.set_camera_orientation(phi=45*DEGREES,theta=-20*DEGREES,zoom=0.8)
        self.add(axes)
        self.play(Write(axes_label))