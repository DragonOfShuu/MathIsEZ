from utils.save_data.save_interpreter import Data
from utils.MathObjects import MathObject
from utils.general_utils import *
from utils.menu import menu 

class PreferenceObject(menu):
    def execute(self):
        pass

class SwitchRadians:
    text = "Switch Angle Measurement Type"
    addon = f"[Switch to {'degrees' if Data().data_raw['is_radians'] else 'radians'}]"
    def execute(self):
        new_data = Data()
        new_data.unsaved["is_radians"] = not new_data.data_raw["is_radians"]
        new_data.save()
        print(f"Now in {'radians' if Data().data_raw['is_radians'] else 'degrees'}")

class PrettyMode:
    text = "Pretty Mode"
    addon = f"[Current value: {'True' if Data().data_raw['pretty_mode'] else 'False'}]"
    def execute(self):
        new_data = Data()
        new_data.unsaved["pretty_mode"] = not new_data.data_raw["pretty_mode"]
        new_data.save()
        print("Now in Pretty Mode" if Data().data_raw['pretty_mode'] else "No longer in pretty mode")

class Preferences(menu):
    text = "Preferences"
    def __init__(self):
        super().__init__([
            SwitchRadians,
            PrettyMode
        ])

# Header menu
class header_menu(menu):
    text = "Header"
    def __init__(self, object_list: list[MathObject | menu]):
        object_list.extend([
            "-",
            Preferences
        ])
        super().__init__(object_list)
    
    def extra(self):
        clear()
        print(f"Currently in {'radians' if Data().data_raw['is_radians'] else 'degrees'}")
        print("What do do?")