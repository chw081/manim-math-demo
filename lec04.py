from manim import *
from manim.utils.color import Colors

class lec04(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45*DEGREES, theta=-35*DEGREES,zoom=0.6)
        self.move_camera(frame_center= [4, -0.5, 1])
        baseCube = Cube(side_length=1, fill_opacity=1, fill_color=RED, stroke_width=0.2, stroke_color=BLACK)
        self.play(FadeIn(baseCube))
        self.play(baseCube.copy().animate(run_time=1.5).shift(RIGHT * 4))
        newCubes = self.createCubes(2, BLUE).shift(UP * 3)
        self.play(FadeIn(newCubes))
        #groups = VGroup(*[newCubes[i].copy() for i in range(0, 2**3, 2)])
        groups = newCubes[0].copy()
        groups2slt1 = VGroup(*[newCubes[1][0].copy(), newCubes[1][1].copy()])
        groups2slt2 = VGroup(*[newCubes[1][2].copy(), newCubes[1][3].copy()])
        self.play(AnimationGroup(*[
            group.animate(run_time=1.5).shift(RIGHT * 5, DOWN * 2) for group in groups]),
            AnimationGroup(*[
            group.animate(run_time=1.5).shift([4, -2, -1]) for group in groups2slt1]),
            AnimationGroup(*[
            group.animate(run_time=1.5).shift([4.5, -3.5, -1]) for group in groups2slt2.rotate(
            90 * DEGREES, axis=[0, 0, 1])]))
        
        newCubes = self.createCubes(3, ORANGE).shift(UP * 8)
        self.play(FadeIn(newCubes))
        #newCubes = self.createCubes(4, GREEN)
        #self.play(FadeIn(newCubes))
    
    #def createLayer(self, n, layerN, newCubes):
    #    return VGroup(*[newCubes[i].copy() for i in range(layerN, n**3, n)])
    
    def layers(self, n, d):
        layers = VGroup()
        for j in range(n):
            layers.add(VGroup(*[d[i] for i in range(j, n**3, n)]))
        return layers
    
    def createCubes(self, n, cColor):
        d = VGroup()
        colorlvl = ['_A', '_B', '_C', '_D', '_E']
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    #layer_color = Colors(cColor) + colorlvl[k]
                    d.add(Cube(side_length=1, fill_opacity=1, fill_color=cColor, stroke_width=0.2, stroke_color=BLACK).shift([i, j, k]))
                #d.add(Cube(side_length=1, fill_opacity=0.5, fill_color=cColor).shift(i*UP, col))
                    #d.add(Cube(side_length=1, fill_opacity=0.5, fill_color=cColor).shift([n - 1, i, j]))
            #d.append(Square(side_length=0.5).shift(i*RIGHT, row))
            #d.append(Square(side_length=0.5).shift(i*UP, col))
        d = self.layers(n, d)
        cubes = d.set_color_by_gradient(cColor, WHITE)
        return cubes.set_stroke(color=BLACK)