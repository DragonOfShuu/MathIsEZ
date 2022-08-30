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