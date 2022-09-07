from utils.general_utils import *
from math import pi, floor

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
    
    def Solve(self) -> float:
        return 0.1;

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