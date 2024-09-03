from manim import *
import numpy as np
from fractions import Fraction

config.disable_caching = True

class SelfAffineFractal(Scene):
    def construct(self):
        w = 4
        h = 2 
        rect1 = Rectangle(width = w, height = h, color = WHITE).to_edge(LEFT, buff = 0.5)
        rect2 = rect1.copy().shift(UP*h)
        rect3 = rect2.copy().shift(RIGHT*w)
        rect4 = rect1.copy().shift(DOWN*h)
        rect5 = rect4.copy().shift(RIGHT*w)
        g1 = VGroup(rect1, rect2, rect3, rect4, rect5)
        g1.center()

        self.add(g1)
        n = 4
        t = 1/n
        for i in range(n):

            self.play(g1.animate.stretch_to_fit_width(g1.width/2), run_time = t)
            self.play(g1.animate.stretch_to_fit_height(g1.height/3), run_time = t)
            self.play(g1.animate.shift(LEFT*g1.width/2))
            i = 1
            g11 = g1
            g22 = g11.copy()
            g33 = g11.copy().shift(UP*g1.height)
            g44 = g11.copy()
            g55 = g44.copy().shift(DOWN*g1.height)

            
            g2 = VGroup(g11, g22, g33, g44, g55)
            #self.play(Write(g11))
            self.play(g22.animate.shift(UP*g1.height), run_time = t)
            self.play(g33.animate.shift(RIGHT*g1.width), run_time = t)
            self.play(g44.animate.shift(DOWN*g1.height), run_time = t)
            self.play(g55.animate.shift(RIGHT*g1.width), run_time = t)

            g2.center()
            g1 = g2
        pass

class SerpinskyCarpet(Scene):
    def construct(self):
        sideLen = 8/3
        s1 = Square(sideLen, fill_opacity = 1).center()
        g1 = VGroup(s1)
        self.add(g1)
        t = 0.1
        n = 4
        g2 = g1.copy()
        for i in range(n):
            g3 = VGroup()
            for mob in g2:
                #s = sideLen/3**(i+1) gives a sodoku like fractal
                s = sideLen/3**(i)
                h1 = mob.copy()
                h2 = mob.copy()
                h3 = mob.copy()
                h4 = mob.copy()
                h5 = mob.copy()
                h6 = mob.copy()
                h7 = mob.copy()
                h8 = mob.copy()

                if (i==0 or i==1):
                    self.play(h1.animate.scale(1/3).shift(UP*s+LEFT*s), run_time = t)
                    self.play(h2.animate.scale(1/3).shift(UP*s), run_time = t)
                    self.play(h3.animate.scale(1/3).shift(UP*s+RIGHT*s), run_time = t)
                    self.play(h4.animate.scale(1/3).shift(LEFT*s), run_time = t)
                    self.play(h5.animate.scale(1/3).shift(RIGHT*s), run_time = t)
                    self.play(h6.animate.scale(1/3).shift(DOWN*s+LEFT*s), run_time = t)
                    self.play(h7.animate.scale(1/3).shift(DOWN*s), run_time = t)
                    self.play(h8.animate.scale(1/3).shift(DOWN*s+RIGHT*s), run_time = t)
                else: 
                    h1.scale(1/3).shift(UP*s+LEFT*s)
                    h2.scale(1/3).shift(UP*s)
                    h3.scale(1/3).shift(UP*s+RIGHT*s)
                    h4.scale(1/3).shift(LEFT*s)
                    h5.scale(1/3).shift(RIGHT*s)
                    h6.scale(1/3).shift(DOWN*s+LEFT*s)
                    h7.scale(1/3).shift(DOWN*s)
                    h8.scale(1/3).shift(DOWN*s+RIGHT*s)    
                     
                g3.add(h1, h2, h3, h4, h5, h6, h7, h8)
                
            g1.add(g3)
            self.add(g3)
            self.wait()
            g2 = g3
            t = t/10
        pass

class FractalTree(Scene):
    def construct(self):
        # g1 contains the entire fractal
        # g2 contains the pieces created in the preceding iterative step
        # g3 contains all new pieces being created in the current step

        d1 = Dot().move_to(DOWN*4)
        d2 = d1.copy().shift(UP*1)
        l1 = Line(start = d1, end = d2, color = WHITE)
        g1 = VGroup(l1) 
        self.play(Write(l1))        
        t = 0.001
        n = 8
        g2 = g1.copy()

        for i in range(n):
            g3 = VGroup()
            for mob in g2:

                l2 = mob.copy().scale(9/10)
                l3 = mob.copy().scale(9/10)


                direction = mob.get_end() - mob.get_start()
                shiftAmt = direction * 0.9

                l2.shift(shiftAmt)
                l3.shift(shiftAmt)

                self.play(l2.animate.rotate(angle = PI/8, about_point = l2.get_start()), run_time = t)
                self.play(l3.animate.rotate(angle = -PI/8, about_point = l3.get_start()), run_time = t)
                
                g3.add(l2, l3)

            g2 = g3
            g1.add(g3)

        
        pass

class KockSnowflake(Scene):
    def construct (self):
        l1 = Line(LEFT*3, RIGHT*3)
        l1.shift(DOWN*2)
        l2 = l1.copy().rotate(PI/3, about_point = l1.get_start())
        l3 = l1.copy().rotate(-PI/3, about_point = l1.get_end())
        l1 = Line(start = l1.get_end(), end = l1.get_start())

        n = 4
        t = 0.01

        #g1 not needed as we dont retain the old configuration 
        g2 = VGroup(l1, l2, l3)

        self.play(Write(l1), Write(l2), Write(l3))
        
        for i in range(n):
            g3 = VGroup()
            for mob in g2:
                
                seg1 = mob.copy().scale(1/3)
                seg2 = mob.copy().scale(1/3)
                direction = mob.get_end()- mob.get_start()

                third1 = Line(start = mob.get_start(), end = mob.get_start()+ direction/3)
                third2 = Line(start = mob.get_end()- direction/3, end = mob.get_end() )
                #self.play(Write(third1), Write(third2))
                self.remove(mob)

                seg1.rotate(PI/3, about_point = seg1.get_start())
                seg2.rotate(-PI/3, about_point = seg2.get_end())
                #self.play(Write(seg1), Write(seg2), run_time = t)
                

                g3.add(third1, seg1, seg2, third2)

            #self.wait(0.5)
            self.play(Write(g3, color = RED))
            self.wait(1)
            self.remove(g2)
            g2 = g3
            
class CesaroCurve(Scene):
    def construct(self):
        plane = ComplexPlane()
        self.add(plane)

        a = complex(0.3, 0.3)

        def c2p(z):
            return(np.array([z.real, z.imag, 0]))
        
        def d0(z):
            #a*z
            return([a.real*z[0]-a.imag*z[1], a.real*z[1]+ a.imag*z[0], 0])
        def d1(z):
            #(a+ (1-a)*z)
            return([a.real+ (1-a).real*z[0]-(1-a).imag*z[1], a.imag+ (1-a).real*z[1]+ (1-a).imag*z[0], 0])
        
        
        z0 = complex(2, 8)
        z1 = complex(-6, -7)
        l = Line(start = c2p(z0), end =c2p(z1), color = WHITE)

        n = 20
    
        def apply_contractions(line, contractions):
            new_lines= VGroup()
            for contraction in contractions:
                points = [line.get_start(), line.get_end()]
                new_points = [contraction(p) for p in points]
                #self.play(*[Write(Dot(point = new_points[i]).scale(0.5)) for i in range(len(new_points))])
                self.add(*[Dot(point = new_points[i]).scale(0.5) for i in range(len(new_points))])
                polyline = VMobject()
                new_line = polyline.set_points_as_corners(new_points)
                #self.play(Write(new_line))
                new_lines.add(new_line)
            return new_lines

        def generateCesaro(line, n):
            if n==0:
                return (VGroup(line))
            llNew = VGroup()
            lNew = apply_contractions(line, [d0, d1])
            for mob in lNew:
                llNew.add(generateCesaro(mob, n-1))
            return(llNew)
        

        generateCesaro(l, n)

class HuchinsonContractionModel(MovingCameraScene):
    def construct (self):

        numLine = NumberLine(include_ticks= True, font_size= 3, line_to_number_buff=0.05, tick_size= 0.005, stroke_width= 0.1)
        endPts = [0, 1]
        #numLine.add_labels(endPts)
        #numLine.scale(10)
        #numLine.center()
        self.add(numLine)
        
        ll = Line(start = [0,0,0], end = [1,0,0], color = GREEN, stroke_width = 1)
        B = VGroup(ll)
        
        #self.add(Dot(point = [0,0,0], color = PINK))

        numMaps = 2
        scales = [1/3, 1/2]
        shifts = [0, 1/2]

        

        maxIter = 5
        fac = 10

        self.camera.frame.shift(RIGHT*1/2).scale(1/fac)

        
        #w1.to_edge(UP/fac+LEFT/fac, buff= 1)
        #w2.next_to(w1, DOWN/fac, buff = 1)

        colors = [GREEN, BLUE]

        def format_as_fraction(value):
            frac = Fraction(value).limit_denominator()
            if frac.denominator == 1:
                return str(frac.numerator)  # Return as integer
            return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
        
        w1 = Tex(f"$W_{1}(x) = {format_as_fraction(scales[0])} x + {format_as_fraction(shifts[0])}$")
        w2 = Tex(f"$W_{2}(x) = {format_as_fraction(scales[1])} x + {format_as_fraction(shifts[1])}$")
       
        w1.shift(UP*3/fac)
        self.add(w1.scale(1/fac/2))
        self.add(w2.scale(1/fac/2).next_to(w1, DOWN/fac, buff = 1/fac))

        self.add(ll)
        self.wait()
        self.remove(ll)

        for i in range(maxIter):
            BNew = VGroup()
            labs = VGroup()
            for k in range(len(B)):
                mob = B[k]
                for j in range(numMaps):

                    l = Line(start = mob.get_start()*scales[j], end = mob.get_end()*scales[j], stroke_width = 1, color = colors[j])
                    l.shift(shifts[j]*RIGHT)

                    s = l.get_start()
                    e = l.get_end()
                    start_value = numLine.p2n(s)
                    end_value = numLine.p2n(e)
                    start_label = MathTex(format_as_fraction(start_value))
                    end_label = MathTex(format_as_fraction(end_value))
                    font_size = 0.025  # Scale factor for font size
                    start_label.scale(font_size)
                    end_label.scale(font_size)

                    endPts.append(start_value)
                    endPts.append(end_value)
                    #print(start_value, end_value)

                    start_label.next_to(numLine.n2p(start_value), 0.1*DOWN)
                    end_label.next_to(numLine.n2p(end_value), 0.1*DOWN)

                    labs.add(start_label, end_label)

                    BNew.add(l)  

            self.remove(B)
            B = BNew
            self.add(BNew)
            self.add(labs)
            self.wait()
            
class BrownianMotion(MovingCameraScene):
    def construct(self):
        self.wait()

class SerpinskyTriangle(Scene):
    def construct(self):
        t1 = Triangle(color = WHITE, stroke_width = 0.75,fill_color = WHITE, fill_opacity = 0.75).scale(4.5)
        gNow = VGroup()
        gPrev = VGroup(t1)
        self.add(t1)
        self.wait()

        maxIter = 8

        for i in range(maxIter):
            gNow = VGroup()
            for t in gPrev:
                verts = t.get_vertices()
                sideLen = np.linalg.norm(verts[0]- verts[1])
                t2 = t.copy().scale(1/2).shift(np.sqrt(3)/8*sideLen*UP)
                t3 = t.copy().scale(1/2).shift(np.sqrt(3)/8*sideLen*DOWN + sideLen/4*LEFT)
                t4 = t.copy().scale(1/2).shift(np.sqrt(3)/8*sideLen*DOWN + sideLen/4*RIGHT)
            
                gNow.add(t2, t3, t4)

            self.clear()
            self.add(gNow)
            self.wait()
            gPrev = gNow

class MidpointTriangleFractal(MovingCameraScene):
    def construct(self):
        w = 6
        h = 9
        t = Polygon([0,0,0], [0,h,0], [w, 0, 0], color = GREEN, fill_color = GREEN, fill_opacity = 0.75)
        #print([0,0,1]/3+ [1,0,0]/2)
        self.camera.frame.shift(UP*4.25 + RIGHT*1.25).scale(1.25)
        self.add(t)
        self.wait()
        scales = []
        shifts = []

        maxIter = 6
        gNow = VGroup()
        gPrev = VGroup(t)

        for i in range(maxIter):
            self.clear()
            gNow = VGroup()
            for t in gPrev:
                verts = t.get_vertices()
                #print("verts are ",i,  verts[0], verts[1], verts[2])
                midPts = [(verts[0]+ verts[1])/2, (verts[1]+ verts[2])/2, (verts[2]+ verts[0])/2]
                #print("mids are ", i,  midPts[0], midPts[1], midPts[2])
                #print("\n")
                t1 = Polygon(verts[0], midPts[0], midPts[2], color = GREEN, fill_color = GREEN, fill_opacity = 0.75)
                t2 = Polygon(midPts[0], verts[1], midPts[1], color = GREEN, fill_color = GREEN, fill_opacity = 0.75)
                t3 = Polygon(midPts[2], midPts[1], verts[2], color = GREEN, fill_color = GREEN, fill_opacity = 0.75)
                gNow.add(t1, t2, t3)
            
            self.add(gNow)
            self.wait()
            gPrev = gNow

class KochCurve(Scene):
    def construct(self):
        
        
        l = Line([-4, 0, 0], [4, 0, 0], color = WHITE)

        self.add(l)
        self.wait()

        gPrev = VGroup(l)
        gNow = VGroup()

        maxIter = 4

        for i in range(maxIter):
            gNow = VGroup()
            for l in gPrev:
                direction =  l.get_start() - l.get_end()
                l1  = l.copy().scale(1/3).shift(direction/3)
                l2 = l.copy().scale(1/3).shift(-direction/3)
                l3 = l.copy().scale(1/3)
                pt = l3.get_start()
                l3.rotate(PI/3, about_point = pt)
                l4 = l.copy().scale(1/3)
                pt = l4.get_end()
                l4.rotate(-PI/3, about_point = pt)

                gNow.add(l1, l3, l4, l2)
                
            self.clear()
            self.play(Write(gNow))
            self.wait()
            gPrev = gNow

class Maps2D(MovingCameraScene):
    def construct(self):
        t1 = Polygon([0,0,0], [1,0,0], [1/2,1,0])
        #r1 = Polygon([0,0,0],[1,0,0], [0,1,0], [1,1,0]).set_color(GREEN)
        self.camera.frame.scale(1.5).shift(RIGHT*6 + UP*4)
        v = t1.get_vertices()
        #rv = r1.get_vertices()
        gNow = VGroup()
        gPrev = VGroup(t1)
        self.add(t1)
        self.wait()
        fac = 1/15
        maxIter = 8



        for i in range(maxIter):
            gNow = VGroup()
            for t in gPrev:
                v = t.get_vertices()

                sideLen = np.linalg.norm(v[0]- v[1])
                t2 = t.copy().scale(1/3).shift(sideLen*RIGHT + sideLen*2*UP).set_color(PURPLE)
                t3 = t.copy().scale(1/5).shift(sideLen*RIGHT + sideLen*3*UP).set_color(GREEN)
                t4 = t.copy().scale(3/4).shift(sideLen*4*RIGHT + sideLen*3*UP).set_color(PINK)
            
                gNow.add(t2, t3, t4)

            self.add(gNow)
            self.wait()
            gPrev = gNow


class Maps2Drect(MovingCameraScene):
    def construct(self):
        r1 = Polygon([0,0,0],[1,0,0], [1,1,0], [0,1,0]).set_color(GREEN)
        self.camera.frame.shift(UP*5+ RIGHT*6).scale(1.5)
        gNow = VGroup()
        gPrev = VGroup(r1)
        self.add(r1)
        self.wait()
        fac = 1/10
        maxIter = 3 



        for i in range(maxIter):
            gNow = VGroup()
            for t in gPrev:
                rv = t.get_vertices()
                
                sideLen = np.linalg.norm(rv[0]- rv[1])
                print(sideLen)

                r2 = t.copy().scale(1/2).shift(sideLen*RIGHT + sideLen*2*UP).set_color(GREEN)
                r3 = t.copy().scale(1/2).shift(sideLen*RIGHT + sideLen*5*UP).set_color(RED)
                r4 = t.copy().scale(1/2).shift(sideLen*5*RIGHT + sideLen*5*UP).set_color(PINK)
                gNow.add(r2, r3, r4)
                #gNow.add(r2)

            self.add(gNow)
            self.wait()
            gPrev = gNow

