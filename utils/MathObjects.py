# from utils.general_utils import *
from utils.general_utils import SuccessionType, give_answer
from math import pi, floor
import logging
# from abc import ABC, abstractmethod

logger = logging.getLogger("program")

# @ABC
class MathObject:
    text = "MathObject default"
    addon = "[]"
    f'''
    text: {text}
    addon: {addon}
    '''
    def execute(self):
        while True:
            try:
                answer = self.Solve()
                if answer == SuccessionType.NO_COPY:
                    break;
                elif answer != SuccessionType.RUN_AGAIN:
                    give_answer(answer)
                    break;
            except ValueError:
                print("\nNot a number.\n")
            except Exception as e:
                logger.exception("An exception has occurred in MathObject:")
                print("\nSomething went wrong. Check your submission information.")
    
    # @abstractmethod
    def Solve(self) -> float: pass
    @classmethod
    def complete(self) -> object: return None

class angle:
    '''
    Class for angles; giving information
    one might need out of the box!

    times_over
    '''
    def __init__(self, value: float | None, is_radians: bool):
        self.is_radians = is_radians 
        self.value = value 
    
    @property 
    def value(self):
        return self._value;
    
    @value.setter
    def value(self, value):
        self._value = value
        if self.is_radians:
            self.times_over = floor(value / 2*pi)
            self.normalized_angle = value % 2*pi 
        else:
            self.times_over = floor(value / 360)
            self.normalized_angle = value % 360