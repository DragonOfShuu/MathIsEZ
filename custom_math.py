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
        return sqrt((b**2)+(c**2)-(2*b*c*cos(angle_a)));

class CosineAngle(MathObject):
    text = "Cosine: Angle"
    addon = "[a, b, c] [SSS]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        b = evaluate(question("side b"))
        c = evaluate(question("side c"))

        return degdec(acos(((b**2)+(c**2)-(a**2))/(2*b*c)));

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
        a = evaluate(question("side a (required)"))
        b = question("side b")
        c = question("side c")

        if (a and b) and not c:
            answer = sqrt((a**2)+(evaluate(b)**2))
        elif (a and c) and not b:
            answer = sqrt((evaluate(c)**2)-(a**2))
        else:
            print("Entered incorrectly. a must have a value, and either b or c has to have a value. b and c cannot simultaneously store a value.")
            logger.debug("User entered incorrect value; A *must* have a value, and either B or C have to hava value. B and C cannot both have a value.")
            return False;
        return answer;

class QuadraticFormula(MathObject):
    text = "Quadratic Formula"
    addon = "[a, b, c]"
    def Solve(self) -> sp.Number:
        a = sympify(question("a"))
        b = sympify(question("b"))
        c = sympify(question("c"))

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
        t_min = float(question("T minimum value"))
        t_max = float(question("T maximum value"))
        t_step = float(question("T step value"))
        x = str(question("Equation for x (t is variable t)="))
        y = str(question("Equation for y (t is variable t)="))
        listx = []
        listy = []
        t_range = np.arange(t_min, t_max+t_step, t_step)
        for t in t_range:
            listx.append(str(eval(x)))
            listy.append(str(eval(y)))
        print("| t | x | y |")
        for count,i in enumerate(t_range):
            print(f"| {i} | {listx[count]} | {listy[count]} |")
        return SuccessionType.NO_COPY;

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

        if not 2 <= len(numbered_objects) <= 20: return problem("You cannot have less than 2 polynomials, or more than 20.")

        x = sp.Symbol('x')
        # Start polynomial using the constant
        polynomial = sympify(c)
        # Add each polynomial term one by one
        for count,i in enumerate(numbered_objects): polynomial += (x**(count+1))*i
        # Solve for x
        zeros = sp.solve(polynomial, x)

        #print equation
        equality("y", polynomial)
        equality("zeroes or xintercepts", zeros)
        return zeros;