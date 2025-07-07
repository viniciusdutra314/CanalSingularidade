from manim import *
import numpy as np




class DotProduct(Scene):
    def _update_angle(self):
        try:
            return Angle(self.vec, self.m_vec, other_angle=True)
        except:
            return None
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_width": 4,
                "stroke_opacity": 0.2
            }
        )
        self.play(Write(number_plane))

        #matrix
        self.M=np.array([[2,3],[0,2]])
        m_matrix = Matrix(self.M)
        tex_H = Tex(r"$H = $", color=WHITE)
        matrix_group = VGroup(tex_H, m_matrix).arrange(RIGHT).to_corner(UL)
        self.play(Write(m_matrix), Write(tex_H))
        
        #initial vectors
        self.delta_s = np.array([1,1])

        self.vec = always_redraw(lambda:
            Vector(self.delta_s, color=GREEN))
        tex_delta_s = always_redraw(lambda :
                                    Tex(r"$\Delta \vec{s}$", color=GREEN).next_to(self.vec.get_end(), RIGHT))
        
        self.add(self.vec, tex_delta_s)
        self.wait(2)        
        self.m_vec = always_redraw(
            lambda: Vector(self.M@(self.vec.get_vector()[:2].T))
        )
        
        tex_H_delta_s = always_redraw(lambda:
            Tex(r"$H \Delta \vec{s}$", color=WHITE).next_to(self.m_vec.get_end()+0.5*UP, RIGHT)
        )
        angle = always_redraw(self._update_angle)

        self.add(self.vec,tex_delta_s)
        self.wait(2)
        self.add(self.m_vec,tex_H_delta_s)
        self.play(TransformFromCopy(self.vec, self.m_vec))
        self.play(FadeIn(angle))
        
        dot_product_tex = MathTex(r"\Delta \vec{s} \cdot H \Delta \vec{s} =", color=WHITE).to_corner(DL)
        dot_product_tex[0][0:3].set_fill(color=GREEN)
        self.play(Write(dot_product_tex))
        dot_product_value = always_redraw(
            lambda: 
            MathTex(f"{np.dot(self.m_vec.get_vector(),self.vec.get_vector()):.2f}", 
                    color=YELLOW).next_to(dot_product_tex, RIGHT))
        
        self.play(Write(dot_product_value))
        self.interactive_embed()
    def on_mouse_press(self, point, button, mods):
        self.delta_s=np.array([point[0], point[1]])

        
