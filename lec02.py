from manim import *


class SameSurface(Scene):
    def construct(self):
        triP1 = [-2, 0, 0] #leftdown
        triP2 = [2, 0, 0] #rightdown
        triP3 = [-5, 4, 0] #up
        point = Dot(point=triP3, radius=0.08)
        point.shift(2*DOWN)
        triangle = Polygon(triP1, triP2, triP3).set_opacity(1).set_color(BLUE)
        triangle.shift(2*DOWN)
        transtriangle = Polygon(triP1, triP2, [5, 4, 0]).set_opacity(1).set_color(BLUE)
        transtriangle.shift(2*DOWN)
        line1 = Line([-8, 2, 0], [8, 2, 0])
        line2 = Line([-8, -2, 0], [8, -2, 0])
        height = DashedLine(triP3, [-5, 0, 0], buff=30, dash_length=0.3, dashed_ratio = 0.7, color=RED).shift(2*DOWN)
        b1 = Brace(height, direction=height.copy().rotate(PI / 2).get_unit_vector())
        #b1text = b1.get_tex("height")
        b1text = Tex(r"高", tex_template=TexTemplateLibrary.ctex).next_to(b1, RIGHT)
        base = Line(triP1, triP2).shift(2*DOWN)

        b2 = Brace(base, direction=base.copy().rotate(3 * PI / 2).get_unit_vector())
        #b2text = b1.get_tex("base")
        b2text = Tex(r"底", tex_template=TexTemplateLibrary.ctex).next_to(b2, DOWN)

        #surfaceText = Tex(r"面积 = 底 $\times$ 高 $\div 2$", tex_template=TexTemplateLibrary.ctex).shift(3*UP)
        t1 = Tex(r"面积", tex_template=TexTemplateLibrary.ctex).shift(3*UP).shift(2*LEFT)
        t2 = MathTex(r" = ", tex_template=TexTemplateLibrary.ctex).next_to(t1)
        t3 = Tex(r"底", tex_template=TexTemplateLibrary.ctex).next_to(t2)
        t4 = MathTex(r" \times ", tex_template=TexTemplateLibrary.ctex).next_to(t3)
        t5 = Tex(r"高", tex_template=TexTemplateLibrary.ctex).next_to(t4)
        t6 = MathTex(r" \div 2").next_to(t5)
        surfaceText = VGroup(t1, t2, t3, t4, t5, t6)

        self.play(FadeIn(line1), FadeIn(line2))
        self.play(FadeIn(triangle), FadeIn(point), FadeIn(height))
        self.play(FadeIn(b1), FadeIn(b1text), FadeIn(b2), FadeIn(b2text), FadeIn(surfaceText))
        self.wait(1)
        self.play(point.animate.shift(10*RIGHT), 
                  Transform(triangle, transtriangle), 
                  height.animate.shift(10*RIGHT), 
                  b1.animate.shift(10*RIGHT),
                  b1text.animate.shift(10*RIGHT), run_time=6)