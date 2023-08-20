from manim import *
from manim.utils.color import Colors

class lec04(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45*DEGREES, theta=-35*DEGREES,zoom=0.6)
        self.move_camera(frame_center= [4, -0.5, 1])
        baseCube = Cube(side_length=1, fill_opacity=1, fill_color=RED, stroke_width=0.2, stroke_color=BLACK)
        transformShift = 5
        prevSum = 0
        self.play(FadeIn(baseCube))
        self.play(baseCube.copy().animate(run_time=1.5).shift(RIGHT * transformShift))
        newCubes = self.createCubes(2, BLUE).shift(UP * 3)
        prevSum += 1
        self.play(FadeIn(newCubes))
        #groups = VGroup(*[newCubes[i].copy() for i in range(0, 2**3, 2)])
        #groups = newCubes[0].copy()
        #groups2slt1 = VGroup(*[newCubes[1][0:2].copy()])
        #groups2slt2 = VGroup(*[newCubes[1][2:4].copy()])
        #self.play(
            #AnimationGroup(*[
            #group.animate(run_time=1.5).shift(RIGHT * 5, DOWN * 2) for group in groups]),
            #groups.animate(run_time=1.5).move_to([5.5, 1.5, 0]),
            #*self.evenSquare(2, newCubes, transformShift, 1),
            #AnimationGroup(*[
            #group.animate(run_time=1.5).shift([4, -2, -1]) for group in groups2slt1]),
            #AnimationGroup(*[
            #group.animate(run_time=1.5).shift([4.5, -3.5, -1]) for group in groups2slt2.rotate(
            #90 * DEGREES, axis=[0, 0, 1])]))
            #groups2slt2.animate(run_time=1.5).move_to([5.5, 0, 0]).rotate(90 * DEGREES, axis=[0, 0, 1]))
        self.play(*self.evenSquare(2, newCubes, transformShift, prevSum))
        newCubes = self.createCubes(3, ORANGE).shift(UP * 7)
        prevSum += 2
        self.play(FadeIn(newCubes))
        self.play(*self.oddSquare(3, newCubes, transformShift, prevSum))
        newCubes = self.createCubes(4, GREEN).shift(UP * 12)
        prevSum += 3
        self.play(FadeIn(newCubes))
        self.play(*self.evenSquare(4, newCubes, transformShift, prevSum))
        newCubes = self.createCubes(5, PURPLE).shift(UP * 18)
        prevSum += 4
        self.play(FadeIn(newCubes))
        self.play(*self.oddSquare(5, newCubes, transformShift, prevSum))
        newCubes = self.createCubes(6, YELLOW).shift(UP * 30)
        prevSum += 5
        self.play(FadeIn(newCubes))
    
    def evenSquare(self, n, newCubes, transformShift, prevSum):
        groups = []
        rightShift = transformShift + (n - 1)//2 * 0.5 + (n * 3 / 2) * 0.5
        upShift = prevSum + (n - 1) * 0.5
        cubesCopy = newCubes.copy()
        for i in range(n//2):
            group = cubesCopy[i]
            groups.append(group.animate(run_time=1.5).move_to([rightShift + i * n, upShift, 0]))
            #groups.add(AnimationGroup(*[c.animate(run_time=1.5).move_to([transShift+i*n, prevSum, -i]) for c in group]))
        for i in range(n//2, n - 1, 1):
            group = cubesCopy[i]
            groups.append(group.animate(run_time=1.5).move_to([transformShift + upShift, upShift - (i - n//2 + 1) * n, 0]))
        evenSeperateSub1 = VGroup(*[newCubes[-1][0:n**2//2].copy()])
        evenSeperateSub2 = VGroup(*[newCubes[-1][n**2//2:n**2].copy()])
        groups.append(evenSeperateSub1.animate(run_time=1.5).move_to([transformShift + (n - 1)//2 * 0.5, upShift, 0]))
        groups.append(evenSeperateSub2.animate(run_time=1.5).move_to([transformShift + upShift, (n - 1)//2 * 0.5, 0]).rotate(90 * DEGREES, axis=[0, 0, 1]))
        return groups
    
    def oddSquare(self, n, newCubes, transformShift, prevSum):
        groups = []
        rightShift = transformShift + n//2
        upShift = prevSum + (n - 1) * 0.5
        cubesCopy = newCubes.copy()
        for i in range(n//2):
            group = cubesCopy[i]
            groups.append(group.animate(run_time=1.5).move_to([rightShift + i * n, upShift, 0]))
        for i in range(n//2, n, 1):
            group = cubesCopy[i]
            groups.append(group.animate(run_time=1.5).move_to([transformShift + upShift, upShift - (i - n//2) * n, 0]))
        return groups
    
    def layers(self, n, d):
        layers = VGroup()
        for j in range(n):
            layers.add(VGroup(*[d[i] for i in range(j, n**3, n)]))
        return layers
    
    def createCubes(self, n, cColor):
        d = VGroup()
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