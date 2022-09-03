from math import pi
from shutil import ExecError
from utils.general_utils import *

class MathObject:
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

# class angle:
#     def __new__(self, value: float | None, is_radians: bool):
#         self.is_radians = is_radians 
#         if self.is_radians:
#             if 0 <= value <= 2*pi: 
#                 self.value = value 
#                 return self;
#             else: raise ValueError(f"Value was not within 0 and 2*pi [Value: {value}]")
#         else:
#             if 0 <= value <= 360