from math import atan, degrees, radians
from utils.save_data.save_interpreter import Data
from fractions import Fraction
from enum import Enum
import sympy as sp
import platform as pf
import functools
import pyperclip
import colorama as col
import logging
import os

logger = logging.getLogger("program")

def deprecated(func):
    '''
    This is for classes that are
    possibly or are going to be
    removed in the future.
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.warning("This method is deprecated; it either will not be available soon, or shouldn't be used.")
        return func(*args, **kwargs);
    return wrapper;

def question(text, /, beckon_text: str = ">>> "):
    print(text)
    returnable = input(beckon_text).strip(" ")
    return returnable

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

@deprecated
def give_answer(value: any):
    try:
        value = round(value, 5)
    except Exception:
        pass
    pyperclip.copy(str(value))
    print(f"Copied: {value}")

@deprecated
def evaluate(value, /, builtInException=True):
    if builtInException: 
        try:
            return float(eval(value))
        except ValueError:
            raise ValueError();
        except Exception as e:
            logger.exception("An error has occurred in evaluate:")
            print("Something went wrong")
    else:
        return float(eval(value));
    
def sympify_exc(value, /, builtInException=True):
    if builtInException:
        try:
            return sp.sympify(value)
        except sp.SympifyError:
            raise NotANumber;
        except Exception:
            print("Something went wrong...")
            logging.exception("An error has occurred in sympify:")
    return sp.sympify(value)

def request(question_text, /, builtInException: bool = True, accept_none: bool = False) -> any:
    value = question(question_text)
    if accept_none and (value == ''): return None
    # if not builtInException: sp.sympify(value)
    # try:
    #     return sp.sympify(value)
    # except sp.SympifyError:
    #     raise NotANumber
    return sympify_exc(value, builtInException)

def request_boolean(text: str, beckon_text: str = "(y/n)> "):
    while True:
        answer: str = question(text, beckon_text)
        try:
            return stringtobool(answer)
        except ValueError:
            print("That was not a yes or no answer.")

def request_bulk(question_texts: list[str], /, built_in_except: bool = True, allow_none: bool = False) -> list[sp.Number]:
    returnable_list = []
    for i in question_texts:
        returnable_list.append( request(i, builtInException=built_in_except, accept_none=allow_none) )
    return returnable_list

def send(sendable: str, /, prefix: str = "", suffix: str = ""):
    print(f"{prefix} {sendable} {suffix}")

def equality(variable: str, value: sp.Number | sp.Expr | str):
    if (Data().data_raw["pretty_mode"]):
        print()
        print(f"{variable} = ")
        sp.pprint(value)
        return;
    print(f"{variable} = {value}")

def problem(text: str, /, color: bool = True, log: bool = True):
    print(f"\n{col.Fore.RED if color else ''}> {text}{col.Fore.WHITE}")
    if log: logger.warn(text)
    return SuccessionType.RUN_AGAIN;
    
@deprecated
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

@deprecated
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

class SuccessionType(Enum):
    NO_COPY = "_no_copy"
    RUN_AGAIN = "_run_again"

class NotANumber(Exception):
    def __init__(self):
        super.__init__()