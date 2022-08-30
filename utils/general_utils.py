from math import atan, degrees, radians
from utils.save_data.save_interpreter import Data
from fractions import Fraction
import platform as pf
import pyperclip
import os

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
    pyperclip.copy(str(value))
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
    return (value if Data().data_raw['is_radians'] else radians(value));

def degdec(value):
    '''
    Decides if the value outputted needs
    to be in converted into degrees.
    '''
    return value if Data().data_raw['is_radians'] else degrees(value);

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
    
    tangle = radians(tangle) if Data().data_raw['is_radians'] else tangle
    return (main_angle, tangle);