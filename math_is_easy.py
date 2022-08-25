from __future__ import annotations

# =============
#  = Modules =
# =============

import sys

if sys.version_info < (3, 10):
    print("Python version is not supported! Only 3.10 and above is supported!")
    sys.exit(1)

import os

def download_module(module_name: str):
    '''
    Downloads a module from the internet.
    '''
    if os.system(f"pip{sys.version_info.major}.{sys.version_info.minor} install {module_name}") == 0:
        print(f"Module {module_name} downloaded!")
    else:
        raise ValueError("Module not found!")


# Evaluate the presence of non-built-in modules
modules_not_found = []

try:
    import pyclip
except ModuleNotFoundError:
    modules_not_found.append("pyclip")

try:
    import numpy as np
except ModuleNotFoundError:
    modules_not_found.append("numpy")

try:
    import sympy as sp
except ModuleNotFoundError:
    modules_not_found.append("sympy")

if modules_not_found:
    print("The following packages could not be located:")
    for i in modules_not_found:
        print(f" - {i}")
    if input("Would you like to download them now? (y/n) > ").lower() == "y":
        for i in modules_not_found:
            download_module(i)
        print("All packages downloaded!")
        print("Restarting...")
        os.system(f"python3 {os.path.basename(__file__)}")
        sys.exit(0)
    else:
        print("Please install the missing packages manually.")
        sys.exit(1)

# Import the rest of the modules
import platform as pf
from math import asin, atan, degrees, sin, sqrt, radians, cos, acos, pi
from fractions import Fraction

is_radians = False

# =============
# = Functions =
# =============

def question(text, /, beckon_text: str = ">>> "):
    print(text)
    returnable = input(beckon_text).strip(" ")
    return returnable;

def clear():
    if pf.system() == "Windows": os.system("cls")
    else: os.system("clear")

def etc():
    input("<Press Enter to Contine>")

def stringtobool(string: str):
    '''
    Converts a string to a boolean.
    '''
    true_strings = ["true", "t", "yes", "y", "1"]
    false_strings = ["false", "f", "no", "n", "0"]
    if string.lower() in true_strings: return True
    elif string.lower() in false_strings: return False
    else: raise ValueError();

def give_answer(value: float):
    value = round(value, 5)
    pyclip.copy(str(value))
    print(f"Answer is {value} [copied!]")
    return "ez";

def evaluate(value, /, builtInException=True):
    if builtInException: 
        try:
            return float(eval(value))
        except ValueError:
            raise ValueError();
        except Exception:
            print("Something went wrong")
    else:
        return float(eval(value));

def fraction_to_string(frac: Fraction):
    '''
    Converts a fraction to a string.
    '''
    return str(frac.numerator) + "/" + str(frac.denominator)

def raddec(value):
    '''
    Decides if the value inputted
    needs to be converted into radians.
    '''
    return (value if is_radians else radians(value));

def degdec(value):
    '''
    Decides if the value outputted needs
    to be in converted into degrees.
    '''
    return value if is_radians else degrees(value);

def get_angle(a: float, b: float):
    '''
    returns (main_angle, angle)

    Main angle being the reference angle (always +), and
    the angle is the angle from between I and IV quadrants.
    '''
    main_angle = degrees(atan(abs(a)/abs(b)))
    # Quadrant II
    if a < 0 and b > 0: tangle = 180 - main_angle 
    # Quadrant III
    elif a < 0 and b < 0: tangle = 180 + main_angle
    #Quandrant IV
    elif a > 0 and b < 0: tangle = 360 - main_angle
    # Up
    elif a == 0 and b > 0: tangle = 90
    # Down
    elif a == 0 and b < 0: tangle = 270
    # Left
    elif a < 0 and b == 0: tangle = 180
    # Right 
    elif a > 0 and b == 0: tangle = 0
    else: tangle = main_angle
    
    tangle = radians(tangle) if is_radians else tangle
    return (main_angle, tangle);

# ===================
# = Base Math Class =
# ===================

class while_run:
    text = "while_run default"
    addon = "[]"
    f'''
    text: {text}
    addon: {addon}
    '''
    def execute(self):
        while True:
            try:
                answer = self.Solve()
                if answer != False:
                    give_answer(answer)
                    break;
            except ValueError:
                print("\nNot a number.\n")
            except Exception as e:
                print("\nSomething went wrong.")
                stringtobool(question("Would you like to see the error? [y/n]"))
    
    def Solve(self) -> float:
        return 0.1;

# ================
# = Trigonometry =
# ================

class HeronEquation(while_run):
    text = "Heron's Equation"
    addon = "[a, b, c] [SSS]"
    def Solve(self) -> float:
        a, b, c = evaluate(Questionnaire([
            "Give side a",
            "Give side b",
            "Give side c"
        ]))

        s = (a+b+c)/2
        return round(sqrt(s*(s-a)*(s-b)*(s-c)), 3);

class CosineSide(while_run):
    text = "Cosine: Side"
    addon = "[b, c, A] [SSA]"
    def Solve(self) -> float:
        b = evaluate(question("side b"))
        c = evaluate(question("side c"))
        angle_a = raddec(evaluate(question("angle a")))
        return sqrt((b**2)+(c**2)-(2*b*c*cos(angle_a)));

class CosineAngle(while_run):
    text = "Cosine: Angle"
    addon = "[a, b, c] [SSS]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        b = evaluate(question("side b"))
        c = evaluate(question("side c"))

        return degdec(acos(((b**2)+(c**2)-(a**2))/(2*b*c)));

class SineAngle(while_run):
    text = "Sine: Angle"
    addon = "[a, A, b] [SSA]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        angle_a = raddec(evaluate(question("angle A")))
        b = evaluate(question("side b"))

        return degdec(asin((sin(angle_a)*b)/a));

class SineSide(while_run):
    text = "Sine: Side"
    addon = "[a, A, B] [AAS]"
    def Solve(self) -> float:
        a = evaluate(question("side a"))
        angle_a = raddec(evaluate(question("angle A")))
        angle_b = raddec(evaluate(question("angle B")))

        return (a*sin(angle_b))/sin(angle_a);

class PythagoreanTheorem(while_run):
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
            print("Entered incorrectly. a must have a value, and either b or c has to have a value, and either b or c cannot have a value.")
            return False;
        return answer;

class QuadraticFormula(while_run):
    text = "Quadratic Formula"
    addon = "[a, b, c]"
    def Solve(self) -> float:
        a = evaluate(question("a"))
        b = evaluate(question("b"))
        c = evaluate(question("c"))

        positive = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
        negative = (-b - sqrt((b**2)-(4*a*c)))/(2*a)

        print(f"x = {positive} or {negative}")
        print("[Copied Positive]")
        return positive;

class ComplexNumberToTrig(while_run):
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

class TrigToComplexNumber(while_run):
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

class ParametricEquation(while_run):
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
        return 1;

class CountTriangles(while_run):
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
            return 'lktkjfyhvtigwnusdkfnhn boi sufkjc';

# ===========
# = Circles =
# ===========

class CircleArea(while_run):
    text = "Circle Area"
    addon = "[r, angle(optional)]"
    def Solve(self) -> float:
        r = evaluate(question("radius"))
        angle = evaluate(question("angle (leave blank to leave out)"))
        if angle:
            return pi*(r**2)*abs( (angle/(2*pi) if is_radians else angle/360) );
        else:
            return pi*(r**2);

class CircleCircumference(while_run):
    text = "Circle Circumference"
    addon = "[r, angle(optional)]"
    def Solve(self) -> float:
        r = evaluate(question("radius"))
        angle = evaluate(question("angle (leave blank to leave out)"))
        if angle:
            return 2*pi*r*abs( (angle/(2*pi) if is_radians else angle/360) );
        else:
            return 2*pi*r;

class CircleFromCenterAndTangent(while_run):
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
                return False;
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
        print("(copied the radius)")
        return r;

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
                return False;
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
        print("(copied the radius)")
        return r;
        
            

# ==============
# = Other Math =
# ==============

class Graph(while_run):
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
        return 1;

class DistanceFormula(while_run):
    text = "Distance Formula"
    addon = "[x1, y1] [x2, y2]"
    def Answer(self, x1, y1, x2, y2) -> float:
        return sqrt((x2-x1)**2 + (y2-y1)**2);
    def Solve(self) -> float:
        x1 = evaluate(question("x1"))
        y1 = evaluate(question("y1"))
        x2 = evaluate(question("x2"))
        y2 = evaluate(question("y2"))
        return self.Answer(x1, y1, x2, y2);


class EvaluateExpression(while_run):
    text = "Evaluate"
    addon = ""
    def Solve(self) -> float:
        return eval(question("Give an expression."));

# =============
# =  Utility  =
# =============

class switch_radians:
    text = "Switch is_radians"
    addon = ""
    def execute(self):
        global is_radians
        is_radians = not is_radians
        print("Switch successful.")

# Question Classes
class Question:
    '''
    Class for asking a question. If answer_type is None,
    then str(answer) is returned. If beckon_text is None,
    then the default beckon is "> ".
    '''
    def __init__(self, question: str, /, answer_type: None, beckon_text: str = None):
        self.question = question
        self.answer_type = answer_type
        self.beckon_text = beckon_text
    def __str__(self):
        return self.question
    
    def main_question(self, comparable: type, answer: float | int | bool | str):
        try:
            if comparable == type(float):
                return float(answer)
            elif comparable == type(int):
                return int(answer)
            elif comparable == type(bool):
                return stringtobool(answer)
            else:
                return answer;
        except Exception:
            print(f"Not an accepted type. Accepted types are {self.answer_type}")
            return None;

    # Ask various questions
    def execute(self):
        while True:
            print(self.question)
            answer = input("> " if self.beckon_text == None else self.beckon_text)
            comparable = type(str if self.answer_type else self.answer_type)
            
            returnable = self.main_question(comparable, answer)
            if returnable == None:
                continue;
            else:
                return returnable;

class Questionnaire:
    '''
    Class for asking multiple questions. DAnswerType and DBeckonText
    are overriding variables for values that are None.
    '''
    def __init__(self, questions: list[Question | str], /, DAnswerType: type = None, DBeckonText: str = None):
        self.questions = questions
        self.DAnswerType = DAnswerType
        self.DBeckonText = DBeckonText
    def execute(self):
        answers = []
        for question in self.questions:
            # Override values if they are not present
            # in the original question.
            if type(question) == Question:
                if question.answer_type == None:
                    question.answer_type = self.DAnswerType;
                if question.beckon_text == None:
                    question.beckon_text = self.DBeckonText;
            else:
                question = Question(question, self.DAnswerType, self.DBeckonText);

            answers.append(question.execute())
        return answers;

# =========
# = Menus =
# =========

# Base Class Menu
class menu:
    '''
    A menu class to go through while_run classes
    and other menus.
    '''
    text = "Menu"
    addon = "[menu]"
    def __init__(self, object_list: list[while_run | menu]):
        self.object_list = object_list
    
    def execute(self):
        while True:
            self.extra()
            for count,i in enumerate(self.object_list):
                print(f"[{count}] {i.text} {i.addon}")
            print("[-1] Exit")

            try:
                reply = int(question(""))
            except ValueError:
                print("Give an integer!")
                etc()
                continue;
            
            if not -1 <= reply <= len(self.object_list)-1:
                print("Index out of range.")
                etc()
                continue;
            
            if reply == -1:
                return;

            if self.object_list[reply] in while_run.__subclasses__():
                try:
                    self.object_list[reply]().execute()
                except KeyboardInterrupt:
                    print("exited :/")
                input("<Press Enter to Continue>")
            else:
                self.object_list[reply]().execute()
    
    def extra(self):
        print()

# Header menu
class header_menu(menu):
    text = "Header"
    def __init__(self, object_list: list[while_run | menu]):
        object_list.append(switch_radians)
        super().__init__(object_list)
    
    def extra(self):
        clear()
        print(f"Currently in: {'radians' if is_radians else 'degrees'}")
        print("What do do?")

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
        super().__init__([QuadraticFormula, HeronEquation, PythagoreanTheorem])

class trig_graph_menu(menu):
    text = "Graphing"
    def __init__(self):
        super().__init__([Graph, ParametricEquation])

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

class main_menu(header_menu):
    def __init__(self):
        super().__init__([
                circle_menu,
                trig_menu
            ])

if __name__ == "__main__":
    main_menu().execute()
    print("Goodbye :/")