from manim import *

class Intro(Scene):
    def construct(self):
        self.camera.background_color= DARK_BLUE
        snippet_generator=lambda file: Code(file_name=file,tab_width=4, background="window",
                             font="Monospace", line_spacing=1,style='Default').scale(0.75)
        extensions=['py','js','c']
        snippets=[snippet_generator(f'float.{j}') for j in extensions]
        textos_strs=['Python','JavaScript','C/C++']
        textos=[]
        for index, j in enumerate(textos_strs):
            texto=Text(j,color=YELLOW,font='Hey Comic')
            texto=texto.scale(1.5).move_to(snippets[index].get_top())
            texto=texto.shift(UP)
            textos.append(texto)
        initial_text=Text('0.1 + 0.2 ≠ 0.3').scale(2)
        self.play(Write(initial_text))
        self.wait(5)
        self.play(FadeIn(snippets[0]),FadeOut(initial_text),FadeIn(textos[0]))
        self.wait(5)
        for j in range(len(snippets)-1):
            self.play(FadeOut(snippets[j]),FadeIn(snippets[j+1]),
                      FadeOut(textos[j]),FadeIn(textos[j+1]))
            self.wait(5)
