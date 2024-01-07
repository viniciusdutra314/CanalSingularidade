from manim import *
func=lambda u,v:(u+1j*v)**2 -5*(u+1j*v)+6
diff=lambda u,v: 2*(u+1j*v)-5
class axis3d(ThreeDScene):
    def construct(self):
        x0=2+2
        axes=ThreeDAxes()
        surface=Surface(lambda u,v: axes.c2p(u,v,np.abs(func(u,v))),
                        u_range=[-2,3],v_range=[-2,3])
        self.set_camera_orientation(phi=45*DEGREES,theta=-20*DEGREES)
        self.add(axes,surface)
        times=0
        while times<5:
            newton_step = func(x0.real,x0.imag) / diff(x0.real,x0.imag)
            x0 -= newton_step
            self.play(Create ( Dot( axes.c2p(x0.real,x0.imag,np.abs( func( x0.real, x0.imag ) ) )) ))
            times+=1
            if np.abs(newton_step) < 1e-6:break  
        self.interactive_embed()