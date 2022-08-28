import importlib
import platform
import json
import sys
import os

print("Verifying Packages...")

with open("packages.json", "r") as f:
    packages = json.load(f)

performed_install = False
for i in packages.keys():
    print(i)
    print(f"Verifying Package: {i}")
    try:
        importlib.import_module(f"{packages[i].get('import_name')}")
    except ImportError:
        performed_install = True
        pip = f"pip{sys.version_info.major}.{sys.version_info.minor}"
        print(f"{i} is not installed. Installing...")
        if os.system(f'{pip} install "{packages[i].get("import_name")}=={packages[i].get("version")}"') == 1:
            print(f"{i} failed to install. Grabbing latest version instead...")
            if os.system(f'{pip} install "{packages[i].get("import_name")}"') == 1:
                print(f"{i} failed to install. Please install manually.")
                sys.exit(1)
        else:
            print(f"{i} installed successfully.")
            continue

print("All packages verified.")
if performed_install:
    input("Press enter to continue...")
os.system("cls" if platform.system() == "Windows" else "clear")