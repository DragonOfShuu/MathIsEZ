from custom_math import *
from utils.menu import *
from math_is_easy import mainmenu

# ==================
# = Subclass Menus =
# ==================

# = Trig =
class lawofsinecosines(menu):
    text = "Law of sine and cosines"
    def __init__(self):
        super().__init__([SineAngle, SineSide, CosineAngle, CosineSide])

class trig_equations_menu(menu):
    text = "Equations"
    def __init__(self):
        super().__init__([
            QuadraticFormula, 
            # HeronEquation, 
            PythagoreanTheorem
            ])

class trig_graph_menu(menu):
    text = "Graphing"
    def __init__(self):
        super().__init__([Graph, ParametricEquation])

class Polynomials(header_menu):
    text = "Polynomials"
    def __init__(self):
        super().__init__([
            PolynomialGraphing,
            PolynomialGraphing_SolveU
        ])

class trig_menu(header_menu):
    text = "Trig"
    def __init__(self):
        super().__init__([
                # Menus
                lawofsinecosines, 
                trig_equations_menu, 
                trig_graph_menu, 
                # Calculations
                CountTriangles,
                ComplexNumberToTrig,
                TrigToComplexNumber,
                EvaluateExpression
            ])

# = Circles =

class circle_menu(header_menu):
    text = "Circles"
    def __init__(self):
        super().__init__([
                CircleArea, 
                CircleCircumference,
                CircleFromCenterAndTangent
            ])

# = Main Menu =

@mainmenu
class main_menu(header_menu):
    def __init__(self):
        super().__init__([
                circle_menu,
                trig_menu,
                Polynomials
            ])
