from __future__ import annotations
from utils.general_utils import *
from utils.save_data.save_interpreter import Data
from utils.MathObjects import MathObject

# Base Class Menu
class menu:
    '''
    A menu class to go through MathObject classes
    and other menus.
    '''
    text = "Menu"
    addon = "[menu]"
    def __init__(self, object_list: list[MathObject | menu]):
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

            if self.object_list[reply] in MathObject.__subclasses__():
                try:
                    self.object_list[reply]().execute()
                except KeyboardInterrupt:
                    print("exited :/")
                input("<Press Enter to Continue>")
            else:
                self.object_list[reply]().execute()
    
    def extra(self):
        print()