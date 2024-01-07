from manim import *

class transformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,
         show_basis_vectors=False                                  
                                           
                                           )

    def construct(self):       
        self.apply_nonlinear_transformation(self.func)  
        self.wait()
    def func(self, dot):
        return np.array([(dot[0]**2)*0.1,(dot[1]**2)*0.1,dot[2]])