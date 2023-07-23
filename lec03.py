from manim import *

class lec03(MovingCameraScene):
    def construct(self):
        baseSquare = Square(side_length=0.5, fill_opacity=1, fill_color=RED)
        basePoint = baseSquare.get_center()
        b1text = MathTex(r"1 = 1^2", font_size=60).shift(DOWN).shift(RIGHT*0.5)
        #squared = MathTex(r" = 1^2").next_to(b1text, RIGHT)
        self.play(self.camera.frame.animate.move_to([3, 2, 0]))
        d = VGroup()
        d.add(baseSquare)
        self.play(FadeIn(d), FadeIn(b1text))
        #squares = self.createSquares(2)
        #newS = VGroup(*squares)
        newS = self.createSquares(2, BLUE)
        b2text = MathTex(r"1 + 3 = 2^2", font_size=60).align_to(b1text, LEFT).shift(DOWN)
        self.play(FadeIn(newS), Transform(b1text, b2text))
        #self.play(FadeIn(b2text))
        newS = self.createSquares(3, ORANGE)
        b1 = b2text
        b3text = MathTex(r"1 + 3 + 5 = 3^2", font_size=60).align_to(b1text, LEFT).shift(DOWN)
        self.play(FadeIn(newS), Transform(b1text, b3text))
        #self.play(FadeIn(b3text))
        newS = self.createSquares(4, GREEN)
        b4text = MathTex(r"1 + 3 + 5 + 7 = 4^2", font_size=60).align_to(b1text, LEFT).shift(DOWN)
        self.play(FadeIn(newS), Transform(b1text, b4text))
        newS = self.createSquares(5, PURPLE)
        b5text = MathTex(r"1 + 3 + 5 + 7 + 9 = 5^2", font_size=60).align_to(b1text, LEFT).shift(DOWN)
        self.play(FadeIn(newS), Transform(b1text, b5text))
        b6text = MathTex(r"1 + 3 + 5 + \cdots + (2n - 1) = n^2", font_size=60).align_to(b1text, LEFT).shift(DOWN)
        self.play( Transform(b1text, b6text))
    
    def createSquares(self, n, sColor):
        d = VGroup()
        #d = []
        row = (n-1)*UP
        col = (n-1)*RIGHT
        for i in range(n):
            d.add(Square(side_length=0.5, fill_opacity=1, fill_color=sColor).shift(i*RIGHT, row))
            d.add(Square(side_length=0.5, fill_opacity=1, fill_color=sColor).shift(i*UP, col))
            #d.append(Square(side_length=0.5).shift(i*RIGHT, row))
            #d.append(Square(side_length=0.5).shift(i*UP, col))
        return d