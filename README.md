MathIsEZ
=
![Static Badge](https://img.shields.io/badge/version-1.0-red)
![GitHub all releases](https://img.shields.io/github/downloads/DragonOfShuu/MathIsEZ/total)
![GitHub top language](https://img.shields.io/github/languages/top/DragonOfShuu/MathIsEZ)
![GitHub](https://img.shields.io/github/license/DragonOfShuu/MathIsEZ)

A project that helps you do math! Many like to say "it helps you do math homework;" however some minimal mathematical knowledge is required (mainly so you can input the values).

# Why MathIsEZ?

MathIsEZ is a project with many complicated highschool level math concepts. The reason this program is so useful is because you can work with symbolic math, aka using variables inside of equations. Not just that, it can also provide fractional values with out a decimal value `(ex: 3/4 instead of 0.75)`. 

This can be especially useful for repetitive yet obvious math that a teacher may give you for example; you already know the subject perfectly, you know all the terms, you just need the math homework done.

# Usage

Using Menus
-
To use, simply type in a number corresponding to the menu or operation you want to perform. For example:

```
Currently in degrees
What do do?
[0] Circles [menu]
[1] Trig [menu]
[2] Polynomials [menu]

[4] Preferences [menu]
[-1] Exit

>>> 4

[0] Switch Angle Measurement Type [Switch to radians]
[1] Pretty Mode [Current value: True]
[-1] Exit

>>>
```

By pressing 4 and then pressing enter, we are now in the preferences menu.

This is important for if you are intending to use any kind of degree measurements that you have selected the proper measurement for your operation.

In our case, we are currently in `degrees`, and inside the preferences it says `switch to radians`, all meaning we are in degrees. To flip the value, now input `0` to select the `[0] Switch Angle Measurement Type [Switch to radians]` option.

## Entering Values
Entering values may depend on what action you are trying to perform. *`These inconsistenices will be addressed in a future commit`*. 

### V1
Many of the math objects on v1 `require` that you put `sp.` at the beginning of certain functions; such as:
```
sp.sqrt(3)
```
This tells the program to use the `sqrt` function from the `sympy` library.

### V2
All of the math objects on v2 `don't require` any extra work on the functions; such as:
```
sqrt(3)
```
The program already understands that the sqrt function is in use.

> Telling The Difference: You can't. Good luck!

### Other Important Things

Please also note that many of the math objects will guide you a little bit on your answer. **Please listen to them and follow their advice**.

# Running With the Virtual Environment


*Windows*
-
To run the virtual environment, first run this command in an elevated PowerShell window:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then press `y` to say just "yes" (`Yes to all` is unnecessary)

When you open the VSCode integrated terminal by using the plus symbol, or pressing `F5`, it will ask you if it is ok to run the script. Make sure to allow it to always run the script.

Then, when you open the vscode terminal from now on, it should do something like this:

```powershell
PS X:\Assets\Code\MathIsEasy> & x:/Assets/Code/MathIsEasy/.venv/Scripts/Activate.ps1

(.venv) PS X:\Assets\Code\MathIsEasy>
```

The `(.venv)` at the beginning signifies you are running commands within the virtual environment. If this does not show up, you are not within the python environment.

With the virutal environment working you are ready to start using/playing with the project!

*Unix*
- 

Just make sure that the Python Extension is installed, and it should automatically work. If this isn't the case, either create a github issue so we can rectify the issue, or you can message me directly.

*Finally*
-
Make sure that you download the dependencies by using the command:

```bash
pip install -r requirements.txt
```
And then simply run the `math_is_easy.py` file!

```bash
python math_is_easy.py
```