from manim import *
from manim.utils.color import Colors

class lec04(ThreeDScene):
    def construct(self):
        mySquare = Square()
        self.play(FadeIn(mySquare))