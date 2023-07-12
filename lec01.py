from manim import *


class CreateCircle(Scene):
    def construct(self):
        anno = Tex(r"目标：求证圆的周长与直径\\比值", tex_template=TexTemplateLibrary.ctex, font_size=40)
        anno.shift(3*RIGHT)
        circle = Circle(radius=2.0)  # create a circle
        circle.shift(2*LEFT)
        triangle = Triangle().scale(2)
        triangle.shift(2*LEFT).align_to(circle, UP)
        self.play(Create(circle), FadeIn(anno))  # show the circle on screen
        triangleS = triangle.copy()
        triCtext = MathTex(r"C = 3\sqrt{3} \\\frac{C}{d} \approx 2.598", font_size=40)
        triCtext.shift(3*RIGHT)

        #six points
        p1 = circle.point_at_angle(30*DEGREES)
        p2 = circle.point_at_angle(150*DEGREES)
        p3 = circle.point_at_angle(270*DEGREES)
        p4 = circle.point_at_angle(90*DEGREES)
        p5 = circle.point_at_angle(210*DEGREES)
        p6 = circle.point_at_angle(330*DEGREES)

        d = VGroup()
        for i in range(0,6):
            num = i*60
            p = circle.point_at_angle(num*DEGREES)
            d.add(Dot(point=p, radius=0.08))
        points = []
        for i in range(0,6):
            num = i*60
            points += [circle.point_at_angle(num*DEGREES)]

        #s1 = Square(side_length=0.25).move_to(p1)
        #s2 = Square(side_length=0.25).move_to(p2)
        #s3 = Square(side_length=0.25).move_to(p3)
        s1 = Dot(point=p1, radius=0.08)
        s2 = Dot(point=p2, radius=0.08)
        s3 = Dot(point=p3, radius=0.08)
        s4 = Dot(point=p4, radius=0.08)
        s5 = Dot(point=p5, radius=0.08)
        s6 = Dot(point=p6, radius=0.08)
        six_poly = Polygon(p1, p4, p2, p5, p3, p6)
        self.play(Create(triangle), FadeIn(s4), FadeIn(s5), FadeIn(s6), FadeOut(anno))

        self.play(triangleS.animate.set_opacity(0.5).set_fill(BLUE), FadeIn(triCtext))
        
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3))

        sixCtext = MathTex(r"C = 6 \\\frac{C}{d} = 3", font_size=40)
        sixCtext.shift(3*RIGHT)

        l1= Line(p1, p4)
        l2= Line(p4, p2)
        l3= Line(p2, p5)
        l4= Line(p5, p3)
        l5= Line(p3, p6)
        l6= Line(p6, p1)
        lines = VGroup(l1,l2,l3,l4,l5,l6)
        #self.play(Create(l1), Create(l2), Create(l3), Create(l4), Create(l5), Create(l6))

        self.play(Create(lines))
        self.play(FadeOut(triangleS), FadeOut(triangle), FadeOut(triCtext))
        self.play(six_poly.animate.set_opacity(0.5).set_fill(BLUE), FadeIn(sixCtext))

        l7= Line(d[0], p1)
        l8= Line(d[0], p6)
        l9= Line(d[1], p1)
        l10= Line(d[1], p4)
        l11= Line(d[2], p2)
        l12= Line(d[2], p4)
        l13= Line(d[3], p2)
        l14= Line(d[3], p5)
        l15= Line(d[4], p3)
        l16= Line(d[4], p5)
        l17= Line(d[5], p3)
        l18= Line(d[5], p6)

        twellines = VGroup(l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18)

        self.play(FadeIn(d))
        self.play(Create(l7), Create(l8), Create(l9), Create(l10)
                  ,Create(l11), Create(l12), Create(l13), Create(l14)
                  ,Create(l15), Create(l16), Create(l17), Create(l18))
        self.play(FadeOut(sixCtext),FadeOut(six_poly),FadeOut(lines))

        p7 = points[0]
        p8 = points[1]
        p9 = points[2]
        p10 = points[3]
        p11 = points[4]
        p12 = points[5]
        twel_poly = Polygon(p7, p1, p8, p4, p9, p2, p10, p5, p11, p3, p12, p6)
        twelCtext = MathTex(r"C \approx 6.212 \\\frac{C}{d} \approx 3.106", font_size=40)
        twelCtext.shift(3*RIGHT)
        self.play(twel_poly.animate.set_opacity(0.5).set_fill(BLUE), FadeIn(twelCtext))
        
class SolvePi(Scene):
    def construct(self):
        anno = Tex(r"目标：求证圆的周长与直径\\比值", tex_template=TexTemplateLibrary.ctex, font_size=40)
        anno.shift(3*RIGHT)
        circle = Circle(radius=2.0)  # create a circle
        circle.shift(2*LEFT)
        self.play(Create(circle), FadeIn(anno))

        #3 poly
        text_3 = MathTex(r"C = 3\sqrt{3} \\\pi \approx 2.598", font_size=40)
        text_3.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 3, 0)
        
        circLines = self.polyLine(circPoints, 3)
        
        lines_3 = VGroup(*circLines)
        poly_3 = Polygon(*circPoints, color=BLUE)

        dots_3 = VGroup()
        for i in circPoints:
            dots_3.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_3), FadeOut(anno))
        self.play(Create(lines_3))
        self.play(poly_3.animate.set_opacity(0.5).set_fill(BLUE), FadeIn(text_3))
        #self.play(FadeOut(poly_3), FadeOut(text_3), FadeOut(dots_3), FadeOut(lines_3))
        self.play(FadeOut(text_3))

        #6 poly
        text_6 = MathTex(r"C = 6 \\\pi = 3", font_size=40)
        text_6.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 6, 0)
        
        circLines = self.polyLine(circPoints, 6)
        
        lines_6 = VGroup(*circLines)
        poly_6 = Polygon(*circPoints, color=BLUE)

        dots_6 = VGroup()
        for i in circPoints:
            dots_6.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_6))
        self.play(Create(lines_6))
        self.play(poly_6.animate.set_opacity(0.5).set_fill(ORANGE), FadeIn(text_6))
        #self.play(FadeOut(poly_6), FadeOut(text_6), FadeOut(dots_6), FadeOut(lines_6))
        self.play(FadeOut(text_6))

        #12 poly
        text_12 = MathTex(r"C \approx 6.212 \\\pi \approx 3.106", font_size=40)
        text_12.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 12, 0)
        
        circLines = self.polyLine(circPoints, 12)
        
        lines_12 = VGroup(*circLines)
        poly_12 = Polygon(*circPoints, color=BLUE)

        dots_12 = VGroup()
        for i in circPoints:
            dots_12.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_12))
        self.play(Create(lines_12))
        self.play(poly_12.animate.set_opacity(0.5).set_fill(GREEN), FadeIn(text_12))
        #self.play(FadeOut(poly_12), FadeOut(text_12), FadeOut(dots_12), FadeOut(lines_12))
        self.play(FadeOut(text_12))

        #24 poly
        text_24 = MathTex(r"C \approx 6.265 \\\pi \approx 3.133", font_size=40)
        text_24.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 24, 0)
        
        circLines = self.polyLine(circPoints, 24)
        
        lines_24 = VGroup(*circLines)
        poly_24 = Polygon(*circPoints, color=BLUE)

        dots_24 = VGroup()
        for i in circPoints:
            dots_24.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_24))
        self.play(Create(lines_24))
        self.play(poly_24.animate.set_opacity(0.5).set_fill(PURPLE), FadeIn(text_24))
        #self.play(FadeOut(poly_24), FadeOut(text_24), FadeOut(dots_24), FadeOut(lines_24))
        self.play(FadeOut(text_24))

        #48 poly
        text_48 = MathTex(r"C \approx 6.279 \\\pi \approx 3.139", font_size=40)
        text_48.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 48, 0)
        
        circLines = self.polyLine(circPoints, 48)
        
        lines_48 = VGroup(*circLines)
        poly_48 = Polygon(*circPoints, color=BLUE)

        dots_48 = VGroup()
        for i in circPoints:
            dots_48.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_48))
        self.play(Create(lines_48))
        self.play(poly_48.animate.set_opacity(0.5).set_fill(RED), FadeIn(text_48))
        self.play(FadeOut(text_48))

        #96 poly
        text_96 = MathTex(r"C \approx 6.282 \\\pi \approx 3.141", font_size=40)
        text_96.shift(3*RIGHT)

        circPoints = self.polyPoint(circle, 96, 0)
        
        circLines = self.polyLine(circPoints, 96)
        
        lines_96 = VGroup(*circLines)
        poly_96 = Polygon(*circPoints, color=BLUE)

        dots_96 = VGroup()
        for i in circPoints:
            dots_96.add(Dot(point=i, radius=0.08))
        
        self.play(FadeIn(dots_96))
        self.play(Create(lines_96))
        self.play(poly_96.animate.set_opacity(0.5).set_fill(BLUE), FadeIn(text_96))
    
    def polyPoint(self, circle, numDots, rotateDegree):
        p = []
        for i in range(0,numDots):
            num = i*(360/numDots) + rotateDegree
            p += [circle.point_at_angle(num*DEGREES)]
        return p
    
    def polyLine(self, pList, numDots):
        lines = []
        for i in range(0,numDots):
            lines += Line(pList[i], pList[(i + 1)%numDots])
        return lines
        

class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270*DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)
        #square = Square()

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))