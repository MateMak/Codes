from manim import *
import numpy as np

# from manim.animation.animation import _AnimationBuilder
from manim.mobject.mobject import _AnimationBuilder


class Biskece0(Scene):
    def construct(self):
        def backscale(self, scale_factor=1.5, run_time=1):
            return ApplyMethod(
                self.scale,
                scale_factor,
                about_point=self.get_center(),
                rate_func=there_and_back,
                run_time=run_time,
            )

        rows_data = []

        def build_table(rows_data):
            table_data = [
                [
                    Tex(r"\# iterací"),
                    MathTex(r"x_{\min}\phantom{0}"),
                    MathTex(r"x_{\max}\phantom{0}"),
                ]
            ]

            for i, x_min, x_max in rows_data:
                table_data.append(
                    [
                        Integer(i),
                        DecimalNumber(x_min, num_decimal_places=2),
                        DecimalNumber(x_max, num_decimal_places=2),
                    ]
                )

            table = MobjectTable(
                table_data,
                include_outer_lines=True,
                line_config={"stroke_width": 2},
            ).scale(0.6)

            return table

        Mobject.backscale = backscale

        eq_size = 0.8
        big_eq_size = 0.7
        huge_eq_size = 0.65
        superlong_eq_size = 0.5
        startpoint_x = 4.5
        startpoint_y = 2.8
        capter_size = 1
        opacity_killer = 0.6

        ax = Axes(
            x_range=[-2, 2.5, 1],
            y_range=[-3, 3, 2],
            x_length=6,
            y_length=5,
            axis_config={
                "include_numbers": True,
                "tip_shape": StealthTip,
            },
        )

        x_label = ax.get_x_axis_label(
            MathTex("x"),
            edge=RIGHT,
            direction=DOWN,
            buff=0.25,
        )

        y_label = ax.get_y_axis_label(
            MathTex("y"),
            edge=UP,
            direction=LEFT,
            buff=0.25,
        )
        root = -1.0114
        labels = VGroup(x_label, y_label)
        graf = ax.plot(
            lambda x: np.cos(x) - 2**x + x**3 + 1,
            x_range=[-1.5, 1.5],
            color=BLUE,
        )

        graf_green = ax.plot(
            lambda x: np.cos(x) - 2**x + x**3 + 1,
            x_range=[root, 1.5],
            color=GREEN,
        )

        graf_red = ax.plot(
            lambda x: np.cos(x) - 2**x + x**3 + 1,
            x_range=[-1.5, root],
            color=RED,
        )

        graf_red_fix = ax.plot(
            lambda x: np.cos(x) - 2**x + x**3 + 1,
            x_range=[-1.5, -1.3],
            color=RED,
        ).shift(LEFT * 2)
        graf_red_float = ax.plot(
            lambda x: np.cos(-1.3) - 2**-1.3 + (-1.3) ** 3 + 1,
            x_range=[-1.3, root],
            color=RED,
        ).shift(LEFT * 2)

        graf_green_fix = ax.plot(
            lambda x: np.cos(x) - 2**x + x**3 + 1,
            x_range=[-0.5, 1.5],
            color=GREEN,
        ).shift(LEFT * 2)
        graf_green_float = ax.plot(
            lambda x: np.cos(-0.5) - 2**-0.5 + (-0.5) ** 3 + 1,
            x_range=[root, -0.5],
            color=GREEN,
        ).shift(LEFT * 2)

        root_dot = Dot(ax.c2p(root, 0), color=YELLOW).set_z_index(10)

        shiftgroup = VGroup(
            root_dot,
            graf_green,
            graf_red,
            ax,   
            labels,
        )
        kladna_hranice_1 = (
            Line(start=ax.c2p(1, 0 - 2), end=ax.c2p(1, 2), color=GREEN)
            .shift(LEFT * 2)
            .set_opacity(opacity_killer)
        )
        green_dot_4 = Dot(ax.i2gp(1, graf_green_fix), color=GREEN).shift(LEFT * 2)

        zaporna_hranice_ghost = (
            Line(start=ax.c2p(-1.3, 0 - 2), end=ax.c2p(-1.3, 2), color=RED)
            .shift(LEFT * 2)
            .set_opacity(opacity_killer)
        )
        red_dot = (
            Dot(ax.i2gp(-1.3, graf_red_fix), color=RED).set_z_index(10).shift(LEFT * 2)
        )

        self.play(
            shiftgroup.animate.shift(LEFT * 2),
        )

        self.play(
            ax.animate.set_opacity(opacity_killer),
            labels.animate.set_opacity(opacity_killer),
        )

        self.play(
            FadeIn(ax),
            FadeIn(labels),
            FadeIn(graf_green),
            FadeIn(graf_red),
            FadeIn(root_dot),
            FadeOut(graf),
        )
        self.wait()
        self.play(
            FadeIn(graf_green_fix),
            FadeIn(graf_green_float),
            FadeIn(graf_red_float),
            FadeIn(graf_red_fix),
            FadeOut(graf_green),
            FadeOut(root_dot),
            FadeOut(graf_red),
        )
        self.wait()
        self.play(
            Write(kladna_hranice_1),
            Write(zaporna_hranice_ghost),
            FadeIn(red_dot),
            FadeIn(green_dot_4),
        )
        self.wait()
        self.play(
            FadeOut(kladna_hranice_1),
            FadeOut(zaporna_hranice_ghost),
            FadeOut(red_dot),
            FadeOut(green_dot_4),
            FadeOut(graf_green_fix),
            FadeOut(graf_green_float),
            FadeOut(graf_red_float),
            FadeOut(graf_red_fix),
        )
        self.wait()

        kvadratic_graf = ax.plot(
            lambda x: x**2,
            x_range=[-1.5, 1.5],
            color=BLUE,
        )
        kvadratic_graf_label = (
            ax.get_graph_label(
                kvadratic_graf,
                label=MathTex("f(x)=x^2 "),
                x_val=1.4,
                direction=UR,
            )
            .scale(big_eq_size)
            .shift(UP * 0.3 + LEFT * 1)
        )
        kvadratic_root_dot = Dot(ax.c2p(0, 0), color=YELLOW).set_z_index(10)

        self.play(
            Write(kvadratic_graf),
            FadeIn(kvadratic_graf_label),
        )
        self.wait()
        self.play(FadeIn(kvadratic_root_dot))
        self.wait()
        self.play(Flash(kvadratic_root_dot))
        self.wait()
        self.play(kvadratic_graf.animate.set_color(GREEN))
        self.wait()

        self.play(
            FadeOut(kvadratic_graf),
            FadeOut(kvadratic_graf_label),
            FadeOut(kvadratic_root_dot),
        )
        self.wait()

        cos_graf = ax.plot(
            lambda x: 1.5 * np.cos(4 * x),
            x_range=[-1.8, 1.8],
            color=BLUE,
        )
        cos_graf_label = (
            ax.get_graph_label(
                cos_graf,
                label=MathTex("f(x)=1.5cos(4x) "),
                x_val=1.4,
                direction=UR,
            )
            .scale(big_eq_size)
            .shift(UP * 0.8 + LEFT * 2)
        )
        cos_root_dot_1 = Dot(ax.c2p(-3 * np.pi / 8, 0), color=YELLOW).set_z_index(10)
        cos_root_dot_2 = Dot(ax.c2p(-np.pi / 8, 0), color=YELLOW).set_z_index(10)
        cos_root_dot_3 = Dot(ax.c2p(np.pi / 8, 0), color=YELLOW).set_z_index(10)
        cos_root_dot_4 = Dot(ax.c2p(3 * np.pi / 8, 0), color=YELLOW).set_z_index(10)

        zaporna_hranice_cos = Line(
            start=ax.c2p(1, 0 - 2), end=ax.c2p(1, 2), color=RED
        ).set_opacity(opacity_killer)
        red_dot_cos = Dot(ax.i2gp(1, cos_graf), color=RED)
        kladna_hranice_cos = Line(
            start=ax.c2p(-np.pi / 2, -2), end=ax.c2p(-np.pi / 2, 2), color=GREEN
        ).set_opacity(opacity_killer)
        green_dot_cos = Dot(ax.i2gp(-np.pi / 2, cos_graf), color=GREEN).set_z_index(10)

        red_dot_label = (
            MathTex(r"1")
            .scale(big_eq_size)
            .next_to(zaporna_hranice_cos, DOWN)
            .set_color(RED)
        )

        green_dot_label = (
            MathTex(r"-\pi/2")
            .scale(big_eq_size)
            .next_to(kladna_hranice_cos, DOWN)
            .set_color(GREEN)
        )

        kladna_hranice_cos_new = Line(
            start=ax.c2p(1 / 2 - np.pi / 4, -2),
            end=ax.c2p(1 / 2 - np.pi / 4, 2),
            color=GREEN,
        ).set_opacity(opacity_killer)
        green_dot_cos_new = Dot(
            ax.i2gp(1 / 2 - np.pi / 4, cos_graf), color=GREEN
        ).set_z_index(10)

        rovnost_1 = (
            MathTex(r"\frac{1+ (-\frac{\pi }{2})}{2} \approx -0.29 ")
            .scale(big_eq_size)
            .next_to(
                ax,
                RIGHT,
            )
            .shift(RIGHT * 1)
        )

        zaporna_hranice_cos2 = Line(
            start=ax.c2p(0.5, -2), end=ax.c2p(0.5, 2), color=RED
        ).set_opacity(opacity_killer)
        red_dot_cos2 = Dot(ax.i2gp(0.5, cos_graf), color=RED)
        kladna_hranice_cos2 = Line(
            start=ax.c2p(-1.5, -2), end=ax.c2p(-1.5, 2), color=GREEN
        ).set_opacity(opacity_killer)
        green_dot_cos2 = Dot(ax.i2gp(-1.5, cos_graf), color=GREEN).set_z_index(10)

        red_dot_label2 = (
            MathTex(r"0.5")
            .scale(big_eq_size)
            .next_to(zaporna_hranice_cos2, DOWN)
            .set_color(RED)
        )

        green_dot_label2 = (
            MathTex(r"-1.5")
            .scale(big_eq_size)
            .next_to(kladna_hranice_cos2, DOWN)
            .set_color(GREEN)
        )

        zaporna_hranice_cos_new2 = Line(
            start=ax.c2p(-0.5, -2),
            end=ax.c2p(-0.5, 2),
            color=RED,
        ).set_opacity(opacity_killer)
        red_dot_cos_new2 = Dot(ax.i2gp(-0.5, cos_graf), color=RED).set_z_index(10)

        rovnost_2 = (
            MathTex(r"\frac{0.5+ (-1.5)}{2} = -0.5 ")
            .scale(big_eq_size)
            .next_to(
                ax,
                RIGHT,
            )
            .shift(RIGHT * 1)
        )

        self.play(Write(cos_graf), Write(cos_graf_label))
        self.wait()
        self.play(
            FadeIn(cos_root_dot_1),
            FadeIn(cos_root_dot_2),
            FadeIn(cos_root_dot_3),
            FadeIn(cos_root_dot_4),
        )

        self.wait()
        self.play(
            Write(kladna_hranice_cos),
            Write(zaporna_hranice_cos),
            FadeIn(red_dot_cos),
            FadeIn(green_dot_cos),
            FadeIn(red_dot_label),
            FadeIn(green_dot_label),
        )
        self.wait()
        self.play(
            Flash(cos_root_dot_1),
            Flash(cos_root_dot_2),
            Flash(cos_root_dot_3),
            cos_root_dot_4.animate.set_color(WHITE).scale(0.4),
        )
        self.wait()
        self.play(FadeIn(rovnost_1))
        self.wait()
        self.play(
            rovnost_1[0][0:11].animate.set_opacity(0),
            rovnost_1[0][11:]
            .animate.next_to(ax.c2p(1 / 2 - np.pi / 4, -2), DOWN)
            .set_color(GREEN)
            .shift(LEFT * 0.15),
            Write(kladna_hranice_cos_new),
            FadeIn(green_dot_cos_new),
            FadeOut(green_dot_label),
            FadeOut(green_dot_cos),
            FadeOut(kladna_hranice_cos),
        )
        self.wait()
        self.play(
            cos_root_dot_1.animate.set_color(WHITE).scale(0.4),
            cos_root_dot_2.animate.set_color(WHITE).scale(0.4),
            Flash(cos_root_dot_3),
        )

        self.wait()
        self.play(
            FadeOut(kladna_hranice_cos_new),
            FadeOut(zaporna_hranice_cos),
            FadeOut(green_dot_cos_new),
            FadeOut(red_dot_cos),
            FadeOut(red_dot_label),
            FadeOut(rovnost_1[0][11:]),
        )
        self.play(
            cos_root_dot_1.animate.set_color(WHITE).scale(1 / 0.4),
            cos_root_dot_2.animate.set_color(WHITE).scale(1 / 0.4),
            cos_root_dot_3.animate.set_color(WHITE),
            cos_root_dot_4.animate.set_color(WHITE).scale(1 / 0.4),
        )

        self.wait()
        self.play(
            Write(kladna_hranice_cos2),
            Write(zaporna_hranice_cos2),
            FadeIn(red_dot_cos2),
            FadeIn(green_dot_cos2),
            FadeIn(red_dot_label2),
            FadeIn(green_dot_label2),
            cos_root_dot_1.animate.set_color(YELLOW),
            cos_root_dot_2.animate.set_color(YELLOW),
            cos_root_dot_3.animate.set_color(YELLOW),
            cos_root_dot_4.animate.set_color(WHITE).scale(0.4),
        )
        self.wait()
        self.play(
            Flash(cos_root_dot_1),
            Flash(cos_root_dot_2),
            Flash(cos_root_dot_3),
        )
        self.wait()
        self.play(FadeIn(rovnost_2))
        self.wait()
        self.play(
            rovnost_2[0][0:13].animate.set_opacity(0),
            rovnost_2[0][13:].animate.next_to(ax.c2p(-1 / 2, -2), DOWN).set_color(RED),
            FadeIn(red_dot_cos_new2),
            FadeOut(red_dot_label2),
            FadeOut(red_dot_cos2),
            zaporna_hranice_cos2.animate.move_to(zaporna_hranice_cos_new2),
        )

        self.wait()
        self.play(
            cos_root_dot_3.animate.set_color(WHITE).scale(0.4),
            cos_root_dot_2.animate.set_color(WHITE).scale(0.4),
            Flash(cos_root_dot_1),
        )
        self.wait()

        self.play(
            FadeOut(labels),
            FadeOut(ax),
            FadeOut(cos_root_dot_1),
            FadeOut(cos_root_dot_2),
            FadeOut(cos_root_dot_3),
            FadeOut(cos_root_dot_4),
            FadeOut(cos_graf_label),
            FadeOut(cos_graf),
            FadeOut(rovnost_2[0][13:]),
            FadeOut(red_dot_cos_new2),
            FadeOut(zaporna_hranice_cos2),
            FadeOut(green_dot_cos2),
            FadeOut(kladna_hranice_cos2),
            FadeOut(green_dot_label2),
        )
        self.wait()
