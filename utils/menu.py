from __future__ import annotations
from utils.general_utils import *
from utils.save_data.save_interpreter import Data
from utils.MathObject import MathObject

class SwitchRadians:
    text = "Switch is_radians"
    addon = ""
    def execute(self):
        new_data = Data()
        new_data.unsaved["is_radians"] = not new_data.data_raw["is_radians"]
        new_data.save()
        print("Switch successful.")

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

# Header menu
class header_menu(menu):
    text = "Header"
    def __init__(self, object_list: list[MathObject | menu]):
        object_list.append(SwitchRadians)
        super().__init__(object_list)
    
    def extra(self):
        clear()
        print(f"Currently in: {'radians' if Data().data_raw['is_radians'] else 'degrees'}")
        print("What do do?")