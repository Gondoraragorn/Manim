from manimlib import *
from json import loads

class Main(Scene):
    def construct(self):
        grid = NumberPlane()
        d1 = Dot([-1, 1, 0])
        d2 = Dot([0, 2, 0])
        r1 = Rectangle(width=2, height=2)
        c1 = Circle().move_to([-1, 1, 0])
        l1 = Line(d1, d2)
        l1 = Line(d1, d2)

        t1 = Tex("Hello").move_to([-2, 2, 0])
        self.add(grid, d1, t1)
        self.play(ReplacementTransform(d1, c1))
        self.wait()
        self.play(ReplacementTransform(c1, l1))
        self.wait()
        self.play(ReplacementTransform(l1, r1))
        self.add(r1)
        self.play(r1.animate.scale(0.5))

class Graph(Scene):
    def construct(self):
        axes = Axes((-10, 10), (-2, 2))
        axes.add_coordinate_labels()
        d1 = Dot()
        d1.move_to(axes.c2p(0, 0))
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        self.wait()
        self.play(FadeIn(d1, scale=0.5))
        self.wait()
        self.play(d1.animate.move_to(axes.c2p(1,1)))
        self.wait()
        graph = axes.get_graph(
            lambda x: 1/x if x > 1 else np.Infinity,
            x_range=(-10, 10),
            color=BLUE,
            discontinuities=[0, 1]
        )
        graph2 = axes.get_graph(
            lambda x: 1 if x < 1 else np.Infinity,
            color=BLUE
        )
        v_line = always_redraw(lambda: axes.get_v_line(d1.get_bottom()))

        self.play(
            ShowCreation(v_line),
        )
        self.play(
            ShowCreation(graph), 
            ShowCreation(graph2)
        )