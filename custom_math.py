from ast import Expression
from utils.general_utils import *
from utils.questions import *
from utils.save_data.save_interpreter import Data
from math import asin, sin, sqrt, cos, acos, pi
import numpy as np
import sympy as sp

from utils.MathObjects import MathObject

# This object needs work. Solve
# errors because Questionnaire needs
# to evaluate each individual answer.
# Commenting out from the menu
# for now.
class HeronEquation(MathObject):
    text = "Heron's Equation"
    addon = "[a, b, c] [SSS]"
    def Solve(self) -> float:
        a, b, c = evaluate(Questionnaire([
            "Give side a",
            "Give side b",
            "Give side c"
        ]).execute())

        s = (a+b+c)/2
        return round(sqrt(s*(s-a)*(s-b)*(s-c)), 3);

class CosineSide(MathObject):
    text = "Cosine: Side"
    addon = "[b, c, A] [SSA]"
    def Solve(self) -> float:
        b = evaluate(question("side b"))
        c = evaluate(question("side c"))
        angle_a = raddec(evaluate(question("angle a")))
        return sqrt((b**2)+(c**2)-(2*b*c*cos(angle_a)))

class CosineAngle(MathObject):
    text = "Cosine: Angle"
    addon = "[a, b, c] [SSS]"
    def Solve(self) -> float:
        a, b, c = request_bulk(
            [
                "Side a",
                "Side b",
                "Side c"
            ]
        )

        angle_a, angle_b, angle_c = self.complete(a, b, c)

        equality("Angle A", angle_a)
        equality("Angle B", angle_b)
        equality("Angle C", angle_c)

        return angle_a;

    @classmethod
    def complete(cls, a:float, b:float, c:float) -> tuple[float, float, float]:
        angle_a = degdec(acos(((b**2)+(c**2)-(a**2))/(2*b*c)))
        angle_b = degdec(acos(((a**2)+(c**2)-(b**2))/(2*a*c)))
        angle_c = degdec(acos(((b**2)+(a**2)-(c**2))/(2*b*a)))

        return (angle_a, angle_b, angle_c)

class SineAngle(MathObject):
    text = "Sine: Angle"
    addon = "[a, A, b] [SSA]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        angle_a = raddec(evaluate(question("angle A")))
        b = evaluate(question("side b"))

        return degdec(asin((sin(angle_a)*b)/a));

class SineSide(MathObject):
    text = "Sine: Side"
    addon = "[a, A, B] [AAS]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        angle_a = raddec(evaluate(question("angle A")))
        angle_b = raddec(evaluate(question("angle B")))

        return (a*sin(angle_b))/sin(angle_a);

class PythagoreanTheorem(MathObject):
    text = "Pythagorean Theorem"
    addon = "[a, b, or c]"
    def Solve(self) -> float:
        print("Press Enter for nulls. At least two must have values.")
        a, b, c = request_bulk(["side a (required)", "side b", "side c"], allow_none=True)

        if (a and b) and not c:
            return sqrt((a**2)+(b**2))
        elif (a and c) and not b:
            return sqrt((c**2)-(a**2))
        
        print("Entered incorrectly. a must have a value, and either b or c has to have a value. b and c cannot simultaneously store a value.")
        logger.debug("User entered incorrect value; A *must* have a value, and either B or C have to hava value. B and C cannot both have a value.")
        return False;


class QuadraticFormula(MathObject):
    text = "Quadratic Formula"
    addon = "[a, b, c]"
    def Solve(self) -> sp.Number:
        a, b, c = request_bulk(["a", "b", "c"])

        positive, negative = self.Answer(a, b, c)

        print(f"x = {positive} or {negative}")
        print("[Copied Positive]")
        return positive;

    def Answer(self, a: sp.Number, b: sp.Number, c: sp.Number) -> tuple[sp.Number, sp.Number]:
        positive = ((-1*b) + sp.sqrt((b**2)-(4*a*c)))/(2*a)
        negative = ((-1*b) - sp.sqrt((b**2)-(4*a*c)))/(2*a)
        return (positive, negative)

class ComplexNumberToTrig(MathObject):
    text = "Complex Number to trig"
    addon = "[a, b] [a + bi]"
    def Solve(self) -> float:
        '''
        a = x
        b = y
        '''
        a = evaluate(question("number a"))
        b = evaluate(question("number b"))
        # print(c)
        c = sqrt((a**2) + (b**2))

        angle = get_angle(a, b)[1]

        print(f"{c}(cos({angle}) + isin({angle}))")
        return SuccessionType.NO_COPY;

class TrigToComplexNumber(MathObject):
    '''
    r(cos(deg/rad)+isin(deg/rad))
    '''
    text = "Trig to complex number"
    addon = "[r, A] [r(cos(A)+isin(A))]"
    def Solve(self) -> float:
        r = evaluate(question("radius"))
        angle = raddec(evaluate(question("angle")))

        a = r*cos(angle)
        b = r*sin(angle)
    
        print(f"{a} + {b}i")
        return SuccessionType.NO_COPY

class ParametricEquation(MathObject):
    text = "Parametric Equations"
    addon = ""
    def Solve(self) -> float:
        t_min, t_max, t_step, x, y = request_bulk([
            "Give the minimum value of T",
            "Give the maximum value of T",
            "Give the step value for T",
            "Give the equation for x (t is t)",
            "Give the equation for y (t is t)"
        ])

        t = sp.Symbol('t')
        t_range = self._floatable_range(t_min, t_max, t_step)

        listx = self._fill_equations(x, t, t_range)
        listy = self._fill_equations(y, t, t_range)

        print("| t | x | y |")
        for count,i in enumerate( t_range ):
            print(f"| {i} | {listx[count]} | {listy[count]} |")
            
        return SuccessionType.NO_COPY

    @classmethod
    def _fill_equations(cls, equa: sp.Expr, var: sp.Symbol, the_range: list):
        return [equa.subs(var, i) for i in the_range]
            
    @classmethod
    def _floatable_range(cls, start: sp.Expr, stop: sp.Expr, step: sp.Expr):
        num = start
        values = []
        while (num <= stop) if (step >= 0) else (num >= stop):
            values.append(num)
            num+=step
        return values
    
class ParametricToCartesian(MathObject):
    text = "Parametric to Cartesian"
    addon = "[x_equation, y_equation] -> t"
    def Solve(self) -> float:
        x_equation, y_equation = request_bulk([
            "Give the equation for x (t is t)",
            "Give the equation for y (t is t)"
        ])

        t = sp.Symbol('t')
        t_1 = sp.solve(x_equation, t)
        equality()
        t_2 = sp.solve(y_equation, t)

class CountTriangles(MathObject):
    text = "Count Triangles"
    addon = "[Z, z, x]"
    def Solve(self) -> float:
        z = evaluate(question("side z"))
        Z = raddec(evaluate(question("angle Z")))
        x = evaluate(question("side x"))
        height = x*sin(Z)
        if z > x:
            print("There is one triangle")
            return 1;
        elif round(z, 3) == round(x, 3):
            print("There is one triangle")
            return 1;
        elif z < height:
            print("There are no triangles")
            return 0;
        elif height < z < x:
            print("There are TWO triangles")
            return 2;
        else: 
            print("error...")
            return SuccessionType.NO_COPY;

# ===========
# = Circles =
# ===========

class CircleArea(MathObject):
    text = "Circle Area"
    addon = "[r, angle(optional)]"
    def Solve(self) -> float:
        r = evaluate(question("radius"))
        angle = evaluate(question("angle (leave blank to leave out)"))
        if angle:
            return pi*(r**2)*abs( (angle/(2*pi) if Data().data_raw["is_radians"] else angle/360) );
        else:
            return pi*(r**2);

class CircleCircumference(MathObject):
    text = "Circle Circumference"
    addon = "[r, angle(optional)]"
    def Solve(self) -> float:
        r = evaluate(question("radius"))
        angle = evaluate(question("angle (leave blank to leave out) (0-360)"))
        if angle:
            return 2*pi*r*abs( (angle/(2*pi) if Data().data_raw["is_radians"] else angle/360) );
        else:
            return 2*pi*r;

class CircleFromCenterAndTangent(MathObject):
    text = "Circle From Center and Tangent"
    addon = "[Center Coords, tangent expression]"

    def Solve(self) -> float:
        print("Note that any special characters require the SymPy module.")
        print("to use, type 'sp.' first (ex: sp.sqrt())")
        # Ask for Data
        x = evaluate(question("x"))
        y = evaluate(question("y"))
        while True:
            try:
                xory = stringtobool(question("if y = answer y, if x = answer n. [y/n]"))
                break
            except ValueError:
                print("Please enter either 'y' or 'n'.")
                continue;

        if xory:
            answer = str(question("tangent (give an expression using x_sym)", "y = "))
            return self.yequals(x, y, answer);
        
        else:
            answer = str(question("tangent (give an expression using y_sym)", "x = "))
            return self.xequals(x, y, answer);

    def xequals(self, x, y, answer) -> float:
        # Symbolize the vars
        x_sym,y_sym = sp.symbols("x y")

        # Generate the equation
        t_y = t_x = t_orig = eval(answer)
        # Example input: x = 4, y = 3, x = y+2
        try:
            if y_sym not in t_orig.free_symbols:
                raise AttributeError()
            try:
                t_x = t_x.subs(y_sym, y) # 3+2
            except AttributeError:
                print("Error: Make sure you use x_sym, not x")
                logger.debug("User may have used 'x' instead of 'x_sym'")
                return SuccessionType.RUN_AGAIN;
            t_x = sp.Eq(x_sym, t_x) # x = 3+2
            x1 = sp.solve(t_x, x_sym)[0] # x = 5
            y1 = y # y = 3

            # Solve for the point on the x axis
            t_y = sp.Eq(x, t_y) # 4 = y+2
            x2 = x # x = 4
            y2 = sp.solve(t_y, y_sym)[0] # y = 2

            # Average the coordinates
            x_avg = (x1 + x2)/2 # (5+4)/2 = 4.5
            y_avg = (y1 + y2)/2 # (3+2)/2 = 2.5
        except AttributeError:
            x_avg = t_x 
            y_avg = y
            
        # Solve for the radius
        r = abs(sqrt((x_avg-x)**2 + (y_avg-y)**2)) # |sqrt((4.5-4)^2 + (2.5-3)^2)| = |sqrt(0.5)| = 0.7071067811865

        # Print the answer
        print(f"(x + {x*-1})^2 + (y + {y*-1})^2 = {r}^2")
        return SuccessionType.NO_COPY;

    def yequals(self, x, y, answer) -> float:
        # Symbolize the vars
        x_sym,y_sym = sp.symbols("x y")

        # Generate the equation
        t_y = t_x = t_orig = eval(answer)

        # Solve for the point on the y axis
        try:
            if x_sym not in t_orig.free_symbols:
                raise AttributeError()
            try:
                t_x = t_x.subs(x_sym, x)
            except AttributeError:
                print("Error: Make sure you use x_sym, not x")
                logger.debug("User may have used 'x' instead of 'x_sym'")
                return SuccessionType.RUN_AGAIN;
            t_x = sp.Eq(y_sym, t_x)
            x1 = x
            y1 = sp.solve(t_x, y_sym)[0]

            # Solve for the point on the x axis
            t_y = sp.Eq(y, t_y)
            x2 = sp.solve(t_y, x_sym)[0]
            y2 = y

            # Average the coordinates
            x_avg = (x1 + x2)/2
            y_avg = (y1 + y2)/2
        except AttributeError:
            x_avg = x
            y_avg = t_x

        # Find the distance between the center and the average
        r = sp.Abs(sp.sqrt((x_avg-x)**2 + (y_avg-y)**2))
        # r = abs(DistanceFormula().Answer(x_avg, y_avg, x, y))

        # Print the answer
        print(f"(x + {x*-1})^2 + (y + {y*-1})^2 = {r}^2")
        return SuccessionType.NO_COPY;
        
# ==============
# = Other Math =
# ==============

class Graph(MathObject):
    text = "Graph"
    addon = "[x] [y=[equation]]"
    def Solve(self) -> float:
        minimum = float(question("minimum"))
        maximum = float(question("maximum"))
        step = float(question("step"))
        range = np.arange(minimum, maximum, step)
        expression = str(question("Expression (x is x)"))
        print("| x | y |")
        for count,x in enumerate(range):
            print(f"| {x} | {eval(expression)}")
        return SuccessionType.NO_COPY;

class DistanceFormula(MathObject):
    text = "Distance Formula"
    addon = "[x1, y1] [x2, y2]"
    def Answer(self, x1, y1, x2, y2) -> float:
        return sp.sqrt((x2-x1)**2 + (y2-y1)**2);
        
    def Solve(self) -> float:
        x1, x2, y1, y2 = request_bulk(["x1", "x2", "y1", "y2"])
        return self.Answer(x1, y1, x2, y2);

class EvaluateExpression(MathObject):
    text = "Evaluate"
    addon = ""
    def Solve(self) -> float:
        expression = request("Give an expression. (no vars)")

        equality("Symbolic Expression", expression)
        equality("Reduced Expression", expression.evalf())
        return expression;

# ========
# Polynomials
# ========

class StandardToVertex(MathObject):
    text = "Standard to Vertex"
    addon = "[a, b, c]"
    def Solve(self) -> float:
        a,b,c = request(["a", "b", "c"])

        # print("doing h...")
        h = (b*-1)/(2*a)
        # print("doing k...")
        k = a*(h**2) + b*(h) + c

        xinter = QuadraticFormula().Answer(a, b, c)
        yinter = c

        if a < 0:
            Range = f"(-oo, {k}]"
        elif a > 0:
            Range = f"[{k}, oo)"
        else:
            Range = k

        send(f"(h, k)")
        send(f"({h}, {k})")
        equality("y", f"{a}(x + {h*-1})^2 + {k}")
        equality("x intercepts", f"({xinter[0]}, 0), ({xinter[1]}, 0)")
        equality("y intercept", f"(0, {yinter})")
        equality("Range", Range)
        equality("Point of Reference", f"({h+1}, {k*a})")

        return SuccessionType.NO_COPY;
    
class Polynomial_SolveU(MathObject):
    text = "Polynomial Solve for U"
    addon = "[Solve U] [a, b, c, u]"
    def Solve(self) -> float:
        # Define x as a symbol
        x = sp.Symbol('x')

        # Gather a, b, c
        # a = sympify(question("a"))
        # b = sympify(question("b"))
        # c = sympify(question("c"))
        a, b, c = request_bulk(["a", "b", "c"])

        # Gather equation for u
        send("\nx is x\n")
        u = request("u")

        # Using x instead of u; pretend it is u
        equation_u = a*(x**2) + b*(x) + c
        # Solves for u
        u_equals = sp.solve(equation_u, x)
        # Solves for u in the x
        x_equals = [sp.solve(sp.Eq(u_equals[0], u), x), 
                    sp.solve(sp.Eq(u_equals[1], u), x)]

        equality("x", x_equals)
        return x_equals;
    
class SolvePolynomial(MathObject):
    text = "Solve Polynomial"
    addon = "[a, b, c, ...]"
    def Solve(self) -> any:
        c = request("constant")
        send("Press Enter when you are finished entering values.")
        numbered_objects = []
        countable = 1
        while True:
            new_value = request(f"x^{countable}", accept_none=True)

            if new_value == None: break;

            numbered_objects.append(new_value)
            countable += 1

        if not 2 <= len(numbered_objects) <= 20: return problem("You cannot have less than 2 terms, or more than 20.")

        x = sp.Symbol('x')
        # Start polynomial using the constant
        polynomial = sympify_exc(c)
        # Add each polynomial term one by one
        for count,i in enumerate(numbered_objects): polynomial += (x**(count+1))*i
        # Solve for x
        zeros = sp.solve(polynomial, x)
        yintercept = polynomial.subs(x, 0)
        factored = sp.factor(polynomial)

        # Clear screen
        clear()
        # Print equation
        equality("y", polynomial)
        equality("y", factored)
        equality("zeroes or xintercepts", zeros)
        equality("y intercept", yintercept)
        print("\n======")
        SubX(polynomial, x).execute()
        # sp.plot(polynomial, line_color="blue")
        return zeros;

class SubX(MathObject):
    '''
    Substitute X for a different value
    repeatedly until the user requests
    to exit
    '''
    text = ""
    addon = ""
    def __init__(self, expression: sp.Expr, replaced_term: sp.Symbol):
        self.expression = expression
        self.x = replaced_term
    def Solve(self) -> None:
        while True:
            replaceable = request("Insert value (press Enter to exit): ", accept_none=True)
            if replaceable == None: break
            print()
            send(self.expression.subs(self.x, replaceable))
            print()
        return SuccessionType.NO_COPY;

class SolveWave(MathObject):
    text = "Solve Wave"
    addon = "[A, B, Φ, ω]"
    def Solve(self) -> float:
        a: sp.Expr; b: sp.Expr; phi: sp.Expr; omega: sp.Expr;
        
        a, b, phi, omega = request_bulk([
            "Give A",
            "Give B",
            "Give Φ",
            "Give ω"
        ])

        equality("Amplitiude", sp.Abs(a))
        equality("Vertical Shift", b)
        equality("Phase Shift", (phi*-1)/omega)
        equality("Period", sp.Abs( (2*sp.pi)/omega ))
        equality("Range", f"[{(a*-1)+b}, {a+b}]")

        return SuccessionType.NO_COPY;
        

# ==========
# IDENTITIES
# ==========

class SinDifference(MathObject):
    text = "Sin Difference"
    addon = "[α, β, +-]"
    def Solve(self) -> float:
        a,b = request_bulk([
            "Give α",
            "Give β"
        ])

        positive = request_boolean("Are we adding the values?")

        equation_1: sp.Expr = sp.sin(a)*sp.cos(b)
        equation_2: sp.Expr = sp.cos(a)*sp.sin(b)

        answer: sp.Expr = sp.simplify( (equation_1+equation_2) if positive else (equation_1-equation_2) )

        equality("answer (symbolic)", answer)
        equality("Answer (Decimate)", answer.evalf())

        return answer.evalf();

class CosDifference(MathObject):
    text = "Cos Difference"
    addon = "[α, β, +-]"
    def Solve(self) -> float:
        a,b = request_bulk([
            "Give α",
            "Give β"
        ])
        
        # We don't care about the user's opinion; we're
        # obviously gonna do the opposite of that crap--
        # Nah, I'm just kidding, it's part of the equation
        positive = not request_boolean("Are we adding the values?")

        equation_1: sp.Expr = sp.cos(a)*sp.cos(b)
        equation_2: sp.Expr = sp.cos(a)*sp.cos(b)

        answer: sp.Expr = sp.simplify( (equation_1+equation_2) if positive else (equation_1-equation_2) )

        equality("answer (symbolic)", answer)
        equality("Answer (Decimate)", answer.evalf())

        return answer.evalf();

class PolarCoorToCoords(MathObject):
    text = "Polar Coords to Coords"
    addon = "[hyp, Φ]"
    def Solve(self) -> float:
        hyp, theta = request_bulk([
            "Give the hypotenuse",
            "Give the absolute angle"
        ])
        temp_theta = sp.sympify(f"{raddec(theta)}")
        x: sp.Expr = hyp*sp.cos(temp_theta)
        y = hyp*sp.sin(temp_theta)

        equality('x', x)
        equality('x [estimate]', x.evalf())

        equality('y', y)
        equality('y [estimate]', y.evalf())

        return SuccessionType.NO_COPY
    
class MagnitudeOfVector(MathObject):
    text = "Magnitude of Vector"
    addon = "[x, y]"
    def Solve(self) -> float:
        x, y = request_bulk([
            "Give x",
            "Give y"
        ])

        answer = self.complete(x, y)
        equality("answer", answer)

        return answer
    
    @classmethod
    def complete(cls, x, y):
        return sp.sympify(f"sqrt(({x})**2 + ({y})**2)")
    
class DotProduct(MathObject):
    text = "Dot Product"
    addon = "<v1, v2>, <w1, w2>"
    def Solve(self) -> float:
        v1, v2, w1, w2 = request_bulk([
            "Give v1",
            "Give v2",
            "Give w1",
            "Give w2",
        ])
        answer = self.complete(v1, v2, w1, w2)

        equality("answer (exact)", answer)
        equality("answer (predicted)", answer.evalf())
        return answer.evalf()
    
    @classmethod
    def complete(cls, v1, v2, w1, w2) -> sp.Expr:
        return sp.sympify(f"({v1}*{w1}) + ({v2}*{w2})")
    
class VectorOperations(MathObject):
    text = "Vector Operations"
    addon = "[v1, v2, w1, w2] [+, -]"
    def Solve(self) -> float:
        v1, v2, w1, w2 = request_bulk([
            "Give v1",
            "Give v2",
            "Give w1",
            "Give w2",
        ])

        add = request_boolean("Is this add?")
        if add:
            answer = ((v1 + w1), (v2 + w2))
        else:
            answer = ((v1 - w1), (v2 - w2))
        
        equality("answer", answer)
        return answer

class Projection(MathObject):
    text = "Projection"
    addon = "<v1, v2>, <w1, w2>"
    def Solve(self) -> float:
        v1, v2, w1, w2 = request_bulk([
            "Give v1",
            "Give v2",
            "Give w1",
            "Give w2",
        ])
        dot_product = DotProduct.complete(v1, v2, w1, w2)

        proj_w_v = self.project(dot_product, w1, w2)
        proj_v_w = self.project(dot_product, v1, v2)

        in_between = self.in_between(dot_product, MagnitudeOfVector.complete(v1, v2), MagnitudeOfVector.complete(w1, w2))

        equality("Dot Product", dot_product)

        equality("Proj w v", proj_w_v[0])
        equality("Proj w v [factored]", proj_w_v[1])
        equality("Proj w v [predicted]", proj_w_v[2])

        equality("Proj v w", proj_v_w[0])
        equality("Proj v w [factored]", proj_v_w[1])
        equality("Proj v w [predicted]", proj_v_w[2])

        equality("In Between [exact]", in_between)
        equality("In Between [predicted]", in_between.evalf())

        return SuccessionType.NO_COPY
    
    def in_between(self, dot_product, v_magnitude, w_magnitude):
        inner = sp.sympify(f"{dot_product} / ({v_magnitude}*{w_magnitude})")
        before_degrees = sp.acos(inner)
        return sp.deg(before_degrees)
    
    @classmethod
    def project(cls, dot_product, v1, v2) -> tuple[str, tuple[float, float], tuple[float, float]]:
        factor = sp.sympify(f'{dot_product} / (({v1})**2 + ({v2})**2)')
        answer1 = f"{factor}<{v1}, {v2}>"
        answer2 = (factor*v1, factor*v2)
        answer3 = tuple(i.evalf() for i in answer2)
        return (answer1, answer2, answer3)
    
class VectorWork(MathObject):
    text = "Vector Work"
    addon = "[force, distance, angle]"
    def Solve(self) -> float:
        f, d, angle = request_bulk([
            "Give the force",
            "Give the distance",
            "Give the angle"
        ])
        work = self.complete(f, d, sp.rad(angle))
        equality("work", work)
        return work

    @classmethod
    def complete(cls, f, d, angle):
        '''
        Angle should be in radians
        '''
        fd = sp.sympify(f"{f}*{d}")
        return fd*sp.cos(angle)