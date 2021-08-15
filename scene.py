from manim import *

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[-3, 3],
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 1)
            },

            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.01, 1)
            },
            tips=False
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        fx = ax.get_graph(lambda x: np.sin(x), color=BLUE)
        fy = ax.get_graph(lambda y: np.cos(y), color=RED)
        area_2 = ax.get_area(fx, [1, 4],bounded=fy, color=GREY, opacity=0.2)
        self.add(ax, labels, fx, fy, area_2)

class Angle(Scene):
     def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))

class Text(Scene):
    def construct(self):
        text = MathTex("\\frac{d}{dx}f(x) = \\frac{f(x+h) - f(x)}{h} = \\lim_{h \\to 0} f(x)")

        self.play(Write(text))
        self.play(text.animate.shift(-2, -1))
        self.wait()

class MovingSineWave(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[-3, 3],
            x_axis_config={
                "numbers_to_include": np.arange(0, 10.01, 1)
            },

            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.01, 1)
            },
            tips=False
        )
        y = ValueTracker(0)
        def fx1(x=0):
            return ax.get_graph(lambda x: np.sin(x+ y.get_value()) + np.cos(x+ y.get_value()))
        def update_wave(func):
            func.become(
                fx1(y.get_value())
            )
            return func
        fx = fx1()
        fx.add_updater(update_wave)
        self.add(ax, fx)
        self.wait()
        self.play(y.animate.increment_value(2*PI), rate_func=linear)


class threedim(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        grid = NumberPlane()
        x = ValueTracker(0)
        def circle_2(x=1):
            return Sphere(radius=x)
        def circle_updater(func):
            func.become(circle_2(x.get_value()))
        circle = circle_2()
        circle.add_updater(circle_updater)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle, axes, grid)
        self.play(x.animate.increment_value(1))
        self.move_camera(phi=10 * DEGREES)
        self.wait(1)
        self.play(x.animate.increment_value(2))
        self.wait(PI/2)
        self.begin_3dillusion_camera_rotation()
        self.wait(6)
        self.stop_3dillusion_camera_rotation()