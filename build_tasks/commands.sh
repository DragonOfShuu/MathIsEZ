cd .. 
pyinstaller math_is_easy.py --add-data=packages.json:. --hidden-import="pyperclip"
clear
./dist/math_is_easy/math_is_easy