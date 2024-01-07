from manim import *


class axis3d(ThreeDScene):
    def construct(self):
        axes=ThreeDAxes()
        self.set_camera_orientation(phi=45*DEGREES,theta=-20*DEGREES)
        surface=Surface(lambda u,v:np.array([u,v,u**2+v**2]),
                        u_range=[-2,2],v_range=[-2,2],
                        fill_opacity=0.7)
        self.add(axes,surface)
        self.move_camera(phi=45*DEGREES,theta=350*DEGREES,run_time=30,rate_func=linear)