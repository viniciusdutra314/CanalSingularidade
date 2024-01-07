from manim import *

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        helix=ParametricFunction(lambda t:
            np.array([np.sin(t),np.cos(t),t*0.1]),
            t_range=[0,10*np.pi],color=BLUE).set_shade_in_3d(True)
        self.set_camera_orientation(phi=40*DEGREES)
        self.add(ThreeDAxes())
        self.play(Write(helix))
        