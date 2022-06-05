#!/usr/bin/env python
# coding: utf-8

# # Main Program Functions

# In[1]:


# def mainMenu():
# global fancy_equation
# global python_equation
# global equation_diff
    
#     fancy_equation = input("Enter the equation: ")
#     if fancy_equation[0:5] == 'sqrt(' and fancy_equation[-1] == ')':
#         display(Math('Equation: \\%s'%fancy_equation))
#     else:
#         display(Math('Equation: %s'%fancy_equation))

    
#     global error
#     error = float(input('Enter the Error: '))
    
  
#     max_iterations = float(input('Enter Maximum Iterations: '))
    
#     choice = str(input("""Choose the Method using the number label:\n1. Bisection\n2. False Postition\n3. Simple Fixed Point\n4. Newton\n5. Secant\n"""))
    
#     if choice == '1':
#         xL = float(input('Enter xL: '))
#         xU = float(input('Enter xU: '))
#         if checkFunctionHasSolutionOrNot(xL, xU):
#             bisection(xL, xU)
#         else:
#             print("Function has no solution!")
#     elif choice == '2':
#         xL = float(input('Enter xL: '))
#         xU = float(input('Enter xU: '))
#         if checkFunctionHasSolutionOrNot(xL, xU):
#             false_position(xL, xU)
#         else:
#             print("Function has no solution!")
#     elif choice == '3':
#         x_value = float(input('Enter x: '))
#         simplefpoint(x_value)
#     elif choice == '4':
#         xo = float(input('Enter xo: '))
#         newton(xo)
#     elif choice == '5':
#         xi_minus1 = float(input('Enter Xi_-1: '))
#         xi = float(input('Enter x_i: '))
#         secant(xi_minus1, xi)
#     else:
#         print("Wrong Choice!")

# def equation_converter(eq):
#     global x
#     simplifiedEquation = eq.strip()
#     simplifiedEquation = simplifiedEquation.replace('x', '*x')
    
#     if simplifiedEquation[0] == '*':
#         simplifiedEquation = simplifiedEquation.replace('*', '')
        
#     equation_list = []
#     equation_list[:0] = simplifiedEquation # Seprate each character into an item in a list
    
#     # Remove extra spaces in the equation if exists
#     if ' ' in equation_list:
#         equation_list.remove(' ')
    
#     for i in range(len(equation_list)):

#         if (equation_list[i] == '+' or equation_list[i] == '-') and equation_list[i+1] == '*':
#             equation_list[i+1] = ''
            
#     simplifiedEquation = ''.join(equation_list) # Concatenate all list items to equation
#     simplifiedEquation = simplifiedEquation.replace('^', '**')
#     return sym.sympify(simplifiedEquation)

# def f(value):
#     temp_eq = python_equation
#     return round(float(temp_eq.subs(x, value)), 3)

# def f_diff(value):
#     temp_eq_diff = equation_diff
#     return round(float(temp_eq_diff.subs(x, value)), 3)
    

# def checkFunctionHasSolutionOrNot(xL, xU):
#     """Check the function has a solution or not for Bisection and False Position methods."""
#     if (f(xL) * f(xU) < 0):
#         return True
#     else:
#         return False


# # Functions for Five Methods 

# ## Bisection

# In[2]:


def bisection(xL, xU):
    """Calculate Xr and Error values."""
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    solution = []
    index = 1
    
    xR = (xL + xU) / 2
    
    # 1# Iteration
    iteration_counter += 1
#     display(Math('Iteration: %g \\space|\\quad x_l = %g \\quad|\\quad f(x_l) = %g \\quad|\\quad x_u = %g \\quad|\\quad f(x_u) = %g \\quad|\\quad x_r = %g \\quad|\\quad f(x_r) = %g \\quad|\\quad \epsilon_a = ---'
#                 %(iteration_counter, xL, f(xL), xU, f(xU), xR, f(xR))))
    
    if (f(xL) * f(xR)) < 0:
        xU = xR
    else:
        xL = xR
    
    solution.append((index, xL, f(xL), xU, f(xU), xR, f(xR), "---"))
    index += 1
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %xR))
        return solution
            
    while(True):
        iteration_counter += 1
        xR_Old = xR
        xR = (xL + xU) / 2
#         display(Math('Iteration: %g \\space|\\quad x_l = %g \\quad|\\quad f(x_l) = %g \\quad|\\quad x_u = %g \\quad|\\quad f(x_u) = %g \\quad|\\quad x_r = %g \\quad|\\quad f(x_r) = %g \\quad|\\quad \epsilon_a = %g \%%'
#                 %(iteration_counter, xL, f(xL), xU, f(xU), xR, f(xR), round((abs((xR - xR_Old) / xR) * 100), 3))))
        
        solution.append((index, xL, f(xL), xU, f(xU), xR, f(xR), str(round((abs((xR - xR_Old) / xR) * 100), round_entry_value.get()))+"%" ))
        index+=1
        
        if ((abs((xR - xR_Old) / xR) * 100) <= float(error)):
#             display(Math('\nRoot = %s' %xR))
            return solution;

        if (f(xL) * f(xR)) < 0:
            xU = xR;
        else:
            xL = xR;
        
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %xR))
            return solution


# ## False Position Method

# In[3]:


def false_position(xL, xU):
    """Calculate Xr and Error values."""
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    solution = []
    index = 1
    
    xR = xU - ( (f(xU) * (xL - xU)) / (f(xL) - f(xU)) )
    
    # 1# Iteration
    iteration_counter += 1
#     display(Math('Iteration: %g \\space|\\quad x_l = %g \\quad|\\quad f(x_l) = %g \\quad|\\quad x_u = %g \\quad \\quad|\\quad f(x_u) = %g \\quad|\\quad x_r = %g \\quad|\\quad f(x_r) = %g \\quad|\\quad \epsilon_a = ---'
#                 %(iteration_counter, round(xL, 3), f(xL), round(xU, 3), f(xU), round(xR, 3), f(xR))))
    
    if (f(xL) * f(xR)) < 0.0:
        xU = xR
    else:
        xL = xR
        
    solution.append((index, xL, f(xL), xU, f(xU), xR, f(xR), "---"))
    index += 1    
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %xR))
        return solution
            
    while(True):
        iteration_counter += 1
        xR_Old = xR
        xR = xU - ( (f(xU) * (xL - xU)) / (f(xL) - f(xU)) )
        eps = abs((xR - xR_Old) / xR) * 100
#         display(Math('Iteration: %g \\space|\\quad x_l = %g \\quad|\\quad f(x_l) = %g \\quad|\\quad x_u = %g \\quad|\\quad f(x_u) = %g \\quad|\\quad x_r = %g \\quad|\\quad f(x_r) = %g \\quad|\\quad \epsilon_a = %g \%%'
#                 %(iteration_counter, round(xL, 3), f(xL), round(xU, 3), f(xU), round(xR, 3), f(xR), round(eps, 3))))
        
        solution.append((index, xL, f(xL), xU, f(xU), xR, f(xR), str(round(eps, round_entry_value.get()))+"%"))
        index+=1
        
        if (eps <= float(error)):
#             display(Math('\nRoot = %s' %xR))
            return solution;

        if (f(xL) * f(xR)) < 0.0:
            xU = xR;
        else:
            xL = xR;
            
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %xR))
            return solution


# ## Simple Fixed Point

# In[4]:


def simplefpoint(x_value):
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    solution = []
    index = 1
    
    # Iteration 1#
    iteration_counter+=1
    xi = x_value
    xiplus1 = f(xi)
#     display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\space | x_{i+1}=%g \\space|\\space \epsilon_a=-----' 
#                  %(iteration_counter, xi, xiplus1)))
    
    solution.append((index, xi, xiplus1, "---"))
    index += 1
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %xiplus1))
        return solution

    # Iteration 2# 
    iteration_counter+=1
    eps = abs((xiplus1 - xi) / xiplus1) * 100
    xi = xiplus1
    xiplus1 = f(xi)
#     display(Math('\\text{Iteration: }%g \\space|\\space x_i=%g \\space|\\space x_{i+1}=%g \\space|\\space \epsilon_a=%g \%%' 
#                  %(iteration_counter, xi, xiplus1, round(eps, 3))))
    
    solution.append((index, xi, xiplus1, str(round(eps, round_entry_value.get()))+"%"))
    index += 1
    
    if (eps <= float(error)):
#         display(Math('\nRoot = %s' %xiplus1))
        return solution;
    
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %xiplus1))
        return solution
    
    while(eps > float(error)):  
        iteration_counter+=1
        eps = abs((xiplus1 - xi) / xiplus1) * 100
        xi = xiplus1
        xiplus1 = f(xi)
#         display(Math('\\text{Iteration: }%g \\space|\\space x_i=%g \\space|\\space x_{i+1}=%g \\space|\\space \epsilon_a=%g \%%' 
#                      %(iteration_counter, xi, xiplus1, round(eps, 3))))
        
        solution.append((index, xi, xiplus1, str(round(eps, round_entry_value.get()))+"%"))
        index += 1
        
        if (eps <= float(error)):
#             display(Math('\nRoot = %s' %xiplus1))
            return solution;
        
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %xiplus1))
            return solution
    


# ## Newton

# In[5]:


def newton(xo):
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    solution = []
    index = 1
    
    # Iteration #1
    iteration_counter+=1
    xi = xo
#     display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a= -----' 
#                  %(iteration_counter, xi, f(xi), f_diff(xi))))
    
    solution.append((index, xi, f(xi), f_diff(xi), "---"))
    index += 1
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %round(xi, 3)))
        return True
    
    # Iteration #2
    iteration_counter+=1
    xiplus1 = xi - ( f(xi) / f_diff(xi) )
    eps = abs((xiplus1 - xi) / xiplus1) * 100
#     display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a=%g \%%' 
#                  %(iteration_counter, xiplus1, f(xiplus1), f_diff(xiplus1), round(eps, 3))))
    
    solution.append((index, xiplus1, f(xiplus1), f_diff(xiplus1), str(round(eps, round_entry_value.get()))+"%"))
    index += 1
    
    if eps <= float(error):
#         display(Math('\nRoot = %s' %round(xi, 3)))
        return solution
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %round(xi, 3)))
        return solution

    while(eps > float(error)):  
        iteration_counter+=1
        xi = xiplus1
        xiplus1 = xi - ( f(xi) / f_diff(xi) )
        eps = abs((xiplus1 - xi) / xiplus1) * 100
        
#         display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a=%g \%%' 
#                      %(iteration_counter, xiplus1, f(xiplus1), f_diff(xiplus1), round(eps, 3))))
        
        solution.append((index, xiplus1, f(xiplus1), f_diff(xiplus1), str(round(eps, round_entry_value.get()))+"%"))
        index += 1
        
        if eps <= float(error):
#             display(Math('\nRoot = %s' %round(xi, 3)))
            return solution
        
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %round(xi, 3)))
            return True


# ## Secant

# In[6]:


def secant(xi_minus1, xi):
    iteration_counter = 0
    if max_iterations == 0:
        return False

    solution = []
    index = 1
    
    while(True):  
        iteration_counter+=1
        eps = abs((xi - xi_minus1) / xi) * 100
#         display(Math('\\text{Iteration: }%g \\space | \\space x_{i-1}=%g \\quad \\quad \\space | \\space f(x_{i-1})=%g \\space|\\space x_i=%g \\quad | \\space f(x_i)=%g \\space | \\quad \epsilon_a=%g\%%' 
#                      %(iteration_counter, round(xi_minus1, 3), f(xi_minus1), round(xi, 3), f(xi), round(eps, 3))))
        
        if iteration_counter == 0:
                    solution.append((index, round(xi_minus1, 3), f(xi_minus1), round(xi, 3), f(xi), str(round(eps, 3))+"%"))
                    index += 1
        
        xi_old = xi
        xi = xi - ( (f(xi) * (xi_minus1 - xi)) / (f(xi_minus1) - f(xi)) ) 
        xi_minus1 = xi_old
        
        solution.append((index, xi_minus1, f(xi_minus1), xi, f(xi), str(round(eps, round_entry_value.get()))+"%"))
        index += 1
        
        if (eps <= float(error)):
#             display(Math('\nRoot = %s' %round(xi, 3)))
            return solution
        
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %round(xi, 3)))
            return solution


# ## Main Program 

# In[7]:


# mainMenu()

# Testing Functions
# 1. Bisection: -2+7x-5x^2+6x^3 | Xl = 0 | Xu = 1 | e = 10%
# 2. False Position: -26+82.3x-88x^2+45.4x^3-9x^4+0.65x^5 | Xl = 0.5 | Xu = 1 | e = 0.2%
#                    -26+85x-91x^2+44x^3-8x^4+x^5 | Xl = 0.5 | Xu = 1 | e = 10%
#                    -13-20x+19x^2-3x^3 | Xl = -1 | Xu = 0 | e = 1%
# 3. Simple Fixed Point: -0.9x^2+1.7x+2.5 --> sqrt(1.88x+2.77) | x = 5 | e = 0.7%
# 4. Newton: -0.9x^2+1.7x+2.5 | x = 5 | e = 0.7%
# 5. Secant: 2x^3-11.7x^2+17.7x-5 | Xi-1 = 3 | Xi = 4, e = 0.7%


# # GUI Code Starts

# ## Main Window

# In[8]:


from IPython.display import display, Math
import sympy as sym
# GUI Libraries
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image # For images within tkinter
import csv # For Export data to Excel file
from tkinter import filedialog

global python_equation
global equation_diff
global max_iterations

global x
x = sym.symbols('x')

global python_equation
python_equation = ''

def equation_converter(eq):
    try:
        simplifiedEquation = eq.strip()
        simplifiedEquation = simplifiedEquation.replace('x', '*x')

        if simplifiedEquation[0] == '*':
            simplifiedEquation = simplifiedEquation.replace('*', '')

        equation_list = []
        equation_list[:0] = simplifiedEquation # Seprate each character into an item in a list

        # Remove extra spaces in the equation if exists
        if ' ' in equation_list:
            equation_list.remove(' ')

        for i in range(len(equation_list)):

            if (equation_list[i] == '+' or equation_list[i] == '-') and equation_list[i+1] == '*':
                equation_list[i+1] = ''

        simplifiedEquation = ''.join(equation_list) # Concatenate all list items to equation
        simplifiedEquation = simplifiedEquation.replace('^', '**')
        return sym.sympify(simplifiedEquation)
    except:
        return False

def f(value):
    global x
    x = sym.symbols('x')
    temp_eq = python_equation
    return round(float(temp_eq.subs(x, value)), 3)

def f_diff(value):
    global x
    x = sym.symbols('x')
    temp_eq_diff = equation_diff
    return round(float(temp_eq_diff.subs(x, value)), 3)
    

def checkFunctionHasSolutionOrNot(xL, xU):
    """Check the function has a solution or not for Bisection and False Position methods."""
    if (f(xL) * f(xU) < 0):
        return True
    else:
        return False
# Use TkAgg in the backend of tkinter application
matplotlib.use('TkAgg')

root = Tk()
root.title('Equaveler')
root.iconbitmap('./images/equaveler_logo.ico')
width_ = 950
height_ = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width_ / 2)
y = (screen_height / 2) - (height_ / 2)
root.geometry(f'{width_}x{height_}+{int(x)}+{int(y)}') # Window size
root.resizable(0, 0)



# Define a function to get the figure output
def graph(text):
    if equation_checker(entry.get()):
        global python_equation
        global equation_diff
        global x
        x = sym.symbols('x')
        # Get the Entry Input
        tmptext = entry.get()
        python_equation = tmptext
        python_equation = equation_converter(python_equation)
        equation_diff = python_equation.diff(x)
        tmptext = "$"+tmptext+"$"
        # Clear any previous Syntax from the figure
        wx.clear()
        wx.text(0.5, 0.4, tmptext, fontsize = 12, ha="center")
        canvas.draw()
    else:
        entry.delete(0, END)

def change_to_main_frame():
    main_frame.pack()
    input_frame.pack_forget()
    
# def change_to_methods_frame():
#     methods_frame.pack(fill='both', expand=1)
#     main_frame.pack_forget()
    
def change_to_input_frame():
    input_frame.pack(fill='both', expand=1)
    main_frame.pack_forget()

def show_equation_examples():
    help_window2 = Toplevel()
    help_window2.title('Equation Examples')
    help_window2.iconbitmap('./images/equaveler_logo.ico')
    width_ = 270
    height_ = 240
    screen_width = help_window2.winfo_screenwidth()
    screen_height = help_window2.winfo_screenheight()
    x = (screen_width / 2) - (width_ / 2)
    y = (screen_height / 2) - (height_ / 2)
    help_window2.geometry(f'{width_}x{height_}+{int(x)}+{int(y)}') # Window size
    help_window2.resizable(0, 0)
    
    input_equations_image = PhotoImage(file="./images/help.png")
    message = Label(help_window2, text="Enter an equation like...", font=("Helvetica", 12)).pack(pady=10)
    help_equation = Label(help_window2, image=input_equations_image, borderwidth=1, bg="black").pack()
    button_help1 = Button(help_window2, text='Got it!', command=help_window2.destroy).pack(pady=10)
    
    help_window2.mainloop()
    
def show_input_examples():
    help_window1 = Toplevel()
    help_window1.title('Input Examples')
    help_window1.iconbitmap('./images/equaveler_logo.ico')
    width_ = 270
    height_ = 580
    screen_width = help_window1.winfo_screenwidth()
    screen_height = help_window1.winfo_screenheight()
    x = (screen_width / 2) - (width_ / 2)
    y = (screen_height / 2) - (height_ / 2)
    help_window1.geometry(f'{width_}x{height_}+{int(x)}+{int(y)}') # Window size
    help_window1.resizable(0, 0)
    
    input_functions_image = PhotoImage(file="./images/input_functions.png")
    help_table = Label(help_window1, image=input_functions_image, borderwidth=1, bg="black").pack()
    button_help2 = Button(help_window1, text='Got it!', command=help_window1.destroy).pack(pady=10)
    
    help_window1.mainloop()
    
def clear_radio_choice_frame():
    try:
        for widgets in radio_choice_frame.winfo_children():
            widgets.destroy()
    except:
        return
            
def equation_checker(equation):
    if equation_converter(equation):
        return True
    else:
        responce = messagebox.showerror("Error","Equation contains wrong characters!")

def number_checker(number):
    if number.isnumeric():
        return True
    else:
        responce = messagebox.showerror("Error","You must enter a number")
        return False

def radio_button_pressed(clicked):   
    if clicked == "bisection":
        show_bisection()
    elif clicked == "false_pos":
        show_false_position()
    elif clicked == "simple_fix":
        show_simple_fixed_point()
    elif clicked == "newton":
        show_newton()
    elif clicked == "secant":
        show_secant()

def show_bisection():
    global radio_choice_frame
    global choice
    choice = "Bisection"
    clear_radio_choice_frame()
    radio_choice_frame.pack(anchor=W)
    
    xl_Label = Label(radio_choice_frame, text="xl", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xl_Entry = Entry(radio_choice_frame, textvariable=xl_value,  width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    xu_Label = Label(radio_choice_frame, text="xU", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xu_Entry = Entry(radio_choice_frame, textvariable=xu_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
def show_false_position():
    global choice
    choice = "False Position Methos"
    clear_radio_choice_frame()
    radio_choice_frame.pack(anchor=W)
    xl_Label = Label(radio_choice_frame, text="xl", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xl_Entry = Entry(radio_choice_frame, textvariable=xl_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    xu_Label = Label(radio_choice_frame, text="xU", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xu_Entry = Entry(radio_choice_frame, textvariable=xu_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    
def show_simple_fixed_point():
    global choice
    choice = "Simple Fixed Point"
    clear_radio_choice_frame()
    radio_choice_frame.pack(anchor=W)
    x_Label = Label(radio_choice_frame, text="x", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    x_Entry = Entry(radio_choice_frame, textvariable=x_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    
def show_newton():
    global choice
    choice = "Newton"
    clear_radio_choice_frame()
    radio_choice_frame.pack(anchor=W)
    x_Label = Label(radio_choice_frame, text="x", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    x_Entry = Entry(radio_choice_frame, textvariable=x_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    
def show_secant():
    global choice
    choice = "Secant"
    clear_radio_choice_frame()
    radio_choice_frame.pack(anchor=W)
    xi_minus1_Label = Label(radio_choice_frame, text="X(i-1)", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xi_minus1_Entry = Entry(radio_choice_frame, textvariable=xi_minus1_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
    xi_Label = Label(radio_choice_frame, text="Xi", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
    xi_Entry = Entry(radio_choice_frame, width=10, textvariable=xi_value, font=("Helvetica", 12)).pack(padx=120, anchor=W)
    
def round_data(values, number_to_round):
    rounded_result = []
    for item in values:
        rounded_result.append(tuple(map(lambda x: isinstance(x, float) and round(x, int(number_to_round)) or x, item)))
    return rounded_result

def calculate_method():
    global error
    global result
    global max_iterations
    if number_checker(max_iterations_temp.get()):
        max_iterations = int(max_iterations_temp.get())
        if equation_checker(entry.get()):
            error = error_value.get()
            if choice == "Bisection":
                result = bisection(float(xl_value.get()), float(xu_value.get()))
                create_table(choice, result)
            elif choice == "False Position Methos":
                result = false_position(float(xl_value.get()), float(xu_value.get()))
                create_table(choice, result)
            elif choice == "Simple Fixed Point":
                result = simplefpoint(float(x_value.get()))
                create_table(choice, result)
            elif choice == "Newton":
                result = newton(float(x_value.get()))
                create_table(choice, result)
            elif choice == "Secant":
                result = secant(float(xi_minus1_value.get()), float(xi_value.get()))
                create_table(choice, result)
        else:
            responce = messagebox.showerror("Missing Equation","You must enter an equation first!")
            return
    else:
        pass

def create_table(table_type, data):
    data = round_data(data, round_entry_value.get())
    if table_type == "Bisection" or table_type == "False Position Methos":
        bisec_false_table(data)
    elif table_type == "Simple Fixed Point":
        simple_table(data)
    elif table_type == "Newton":
        newton_table(data)
    elif table_type == "Secant":
        secant_table(data)

def bisec_false_table(contents1):
    ws  = Tk()
    ws.iconbitmap('./images/equaveler_logo.ico')
    ws.title(choice + ' Solution')
    ws.geometry('660x280')
    ws.resizable(0, 0)
    ws['bg'] = '#ffab40'
    
    table_frame = Frame(ws)
    

    bisection_table = ttk.Treeview(table_frame, yscrollcommand=1)

    bisection_table['columns'] = ('i', 'xL', 'f(xL)', 'xU', 'f(xU)', 'xR', 'f(xR)', 'eps')

    bisection_table.column("#0", width=0, stretch=NO)
    bisection_table.column("i", anchor=CENTER, width=80)
    bisection_table.column("xL", anchor=CENTER, width=80)
    bisection_table.column("f(xL)", anchor=CENTER, width=80)
    bisection_table.column("xU", anchor=CENTER, width=80)
    bisection_table.column("f(xU)", anchor=CENTER, width=80)
    bisection_table.column("xR", anchor=CENTER, width=80)
    bisection_table.column("f(xR)", anchor=CENTER, width=80)
    bisection_table.column("eps", anchor=CENTER, width=80)

    bisection_table.heading("#0", text="", anchor=CENTER)
    bisection_table.heading("i", text="Id", anchor=CENTER)
    bisection_table.heading("xL", text="xL", anchor=CENTER)
    bisection_table.heading("f(xL)", text="f(xL)", anchor=CENTER)
    bisection_table.heading("xU", text="xU", anchor=CENTER)
    bisection_table.heading("f(xU)", text="f(xU)", anchor=CENTER)
    bisection_table.heading("xR", text="xR", anchor=CENTER)
    bisection_table.heading("f(xR)", text="f(xR)", anchor=CENTER)
    bisection_table.heading("eps", text="eps", anchor=CENTER)

    for index, item in enumerate(contents1):
        bisection_table.insert(parent='',index='end', iid=index,text='', values=item)
    
    scrollbar = Scrollbar(ws, orient=VERTICAL, command=bisection_table.yview)
    bisection_table.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y) 
    
    bisection_table.pack()
    table_frame.pack()
    
    root = contents1[-1][5]
    root_label = Label(ws, foreground='#800020', background='#ffab40',
                       text="Root = "+str(round(root, round_entry_value.get())), 
                       font=("Helvetica", 16, "italic", "bold"))
    root_label.place(x=10, y=240)
    export_image = PhotoImage(file=("./images/export_to_excel_smaller.png"), master=ws)
    csv_button = Button(ws, image=export_image, borderwidth=0, background='#ffab40', activebackground='#ffab40',
                        command=lambda: write_to_csv(contents1))
    csv_button.pack(anchor=S+E, padx=10, pady=10)
    
    ws.mainloop()

def simple_table(contents2):
    ws  = Tk()
    ws.title(choice + ' Solution')
    ws.iconbitmap('./images/equaveler_logo.ico')
    ws.geometry('340x285')
    ws.resizable(0, 0)
    ws['bg'] = '#ffab40'
    
    table_frame = Frame(ws)

    bisection_table = ttk.Treeview(table_frame, yscrollcommand=1)

    bisection_table['columns'] = ('i', 'xL', 'f(xL)', 'eps')

    bisection_table.column("#0", width=0, stretch=NO)
    bisection_table.column("i", anchor=CENTER, width=80)
    bisection_table.column("xL", anchor=CENTER, width=80)
    bisection_table.column("f(xL)", anchor=CENTER, width=80)
    bisection_table.column("eps", anchor=CENTER, width=80)

    bisection_table.heading("#0", text="", anchor=CENTER)
    bisection_table.heading("i", text="Id", anchor=CENTER)
    bisection_table.heading("xL", text="xL", anchor=CENTER)
    bisection_table.heading("f(xL)", text="f(xL)", anchor=CENTER)
    bisection_table.heading("eps", text="eps", anchor=CENTER)

    for index, item in enumerate(contents2):
        bisection_table.insert(parent='',index='end', iid=index,text='', values=item)

    scrollbar = Scrollbar(ws, orient=VERTICAL, command=bisection_table.yview)
    bisection_table.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y) 
    
    bisection_table.pack()
    table_frame.pack()
    
    root = contents2[-1][1]
    root_label = Label(ws, foreground='#800020', background='#ffab40',
                       text="Root = "+str(round(root, round_entry_value.get())), 
                       font=("Helvetica", 16, "italic", "bold"))
    
    root_label.place(x=10, y=240)
    export_image = PhotoImage(file=("./images/export_to_excel_smaller.png"), master=ws)
    csv_button = Button(ws, image=export_image, borderwidth=0, background='#ffab40', activebackground='#ffab40',
                        command=lambda: write_to_csv(contents2))
    csv_button.pack(anchor=S+E, padx=5, pady=10)
    
    ws.mainloop()
    
def newton_table(contents3):
    ws  = Tk()
    ws.title(choice + ' Solution')
    ws.iconbitmap('./images/equaveler_logo.ico')
    ws.geometry('420x285')
    ws.resizable(0, 0)
    ws['bg'] = '#ffab40'
    
    table_frame = Frame(ws)

    bisection_table = ttk.Treeview(table_frame, yscrollcommand=1)

    bisection_table['columns'] = ('i', 'Xi', 'f(Xi)', "f'(Xi)", 'eps')

    bisection_table.column("#0", width=0, stretch=NO)
    bisection_table.column("i", anchor=CENTER, width=80)
    bisection_table.column("Xi", anchor=CENTER, width=80)
    bisection_table.column("f(Xi)", anchor=CENTER, width=80)
    bisection_table.column("f'(Xi)", anchor=CENTER, width=80)
    bisection_table.column("eps", anchor=CENTER, width=80)

    bisection_table.heading("#0", text="", anchor=CENTER)
    bisection_table.heading("i", text="Id", anchor=CENTER)
    bisection_table.heading("Xi", text="Xi", anchor=CENTER)
    bisection_table.heading("f(Xi)", text="f(Xi)", anchor=CENTER)
    bisection_table.heading("f'(Xi)", text="f'(Xi)", anchor=CENTER)
    bisection_table.heading("eps", text="eps", anchor=CENTER)

    for index, item in enumerate(contents3):
        bisection_table.insert(parent='',index='end', iid=index,text='', values=item)
    
    scrollbar = Scrollbar(ws, orient=VERTICAL, command=bisection_table.yview)
    bisection_table.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y) 
    
    bisection_table.pack()
    table_frame.pack()
    
    root = contents3[-1][1]
    root_label = Label(ws, foreground='#800020', background='#ffab40',
                       text="Root = "+str(round(root, round_entry_value.get())), 
                       font=("Helvetica", 16, "italic", "bold"))
    root_label.place(x=10, y=240)
    
    export_image = PhotoImage(file=("./images/export_to_excel_smaller.png"), master=ws)
    csv_button = Button(ws, image=export_image, borderwidth=0, background='#ffab40', activebackground='#ffab40',
                        command=lambda: write_to_csv(contents3))
    csv_button.pack(anchor=S+E, padx=10, pady=10)
    
    ws.mainloop()
    
def secant_table(contents4):
    ws  = Tk()
    ws.title(choice + ' Solution')
    ws.iconbitmap('./images/equaveler_logo.ico')
    ws.geometry('500x280')
    ws.resizable(0, 0)
    ws['bg'] = '#ffab40'

    table_frame = Frame(ws)

    bisection_table = ttk.Treeview(table_frame, yscrollcommand=1)

    bisection_table['columns'] = ('i', 'X(i-1)', 'f(X(i-1))', 'Xi', "f(Xi)", 'eps')

    bisection_table.column("#0", width=0, stretch=NO)
    bisection_table.column("i", anchor=CENTER, width=80)
    bisection_table.column("X(i-1)", anchor=CENTER, width=80)
    bisection_table.column('f(X(i-1))', anchor=CENTER, width=80)
    bisection_table.column("Xi", anchor=CENTER, width=80)
    bisection_table.column("f(Xi)", anchor=CENTER, width=80)
    bisection_table.column("eps", anchor=CENTER, width=80)

    bisection_table.heading("#0", text="", anchor=CENTER)
    bisection_table.heading("i", text="Id", anchor=CENTER)
    bisection_table.heading("X(i-1)", text="X(i-1)", anchor=CENTER)
    bisection_table.heading('f(X(i-1))', text='f(X(i-1))', anchor=CENTER)
    bisection_table.heading("Xi", text="Xi", anchor=CENTER)
    bisection_table.heading("f(Xi)", text="f(Xi)", anchor=CENTER)
    bisection_table.heading("eps", text="eps", anchor=CENTER)

    for index, item in enumerate(contents4):
        bisection_table.insert(parent='',index='end', iid=index,text='', values=item)
    
    scrollbar = Scrollbar(ws, orient=VERTICAL, command=bisection_table.yview)
    bisection_table.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    bisection_table.pack()
    table_frame.pack()
    
    root = contents4[-1][3]
    root_label = Label(ws, foreground='#800020', background='#ffab40',
                       text="Root = "+str(round(root, round_entry_value.get())), 
                       font=("Helvetica", 16, "italic", "bold"))
    root_label.pack(pady=10, padx=10, anchor=S+W)
    
    export_image = PhotoImage(file=("./images/export_to_excel_smaller.png"), master=ws)
    csv_button = Button(ws, image=export_image, borderwidth=0, background='#ffab40', activebackground='#ffab40',
                        command=lambda: write_to_csv(contents4))
    csv_button.place(x=420, y=235)
    
    ws.mainloop()
    
def write_to_csv(csv_data):
    if choice == "Bisection":
        fields=['i', 'xL', 'f(xL)', 'xU', 'f(xU)', 'xR', 'f(xR)', 'eps']
    elif choice == "False Position Methos":
        fields=['i', 'xL', 'f(xL)', 'xU', 'f(xU)', 'xR', 'f(xR)', 'eps']
    elif choice == "Simple Fixed Point":
        fields=['i','Xi','f(Xi)', 'eps']
    elif choice == "Newton":
        fields=['i','Xi','f(Xi)', "f'(Xi)", 'eps']
    elif choice == "Secant":
        fields=['i','X(i-1)','Xi', 'f(Xi)', 'eps']
    
    myfile = filedialog.asksaveasfile(defaultextension='.csv', title= "Select file", filetypes = [("CSV File",".csv"),])
    w = csv.writer(myfile, dialect='excel')
    w.writerow(fields)
    for record in csv_data:
        w.writerow(record)
    myfile.close()
    
            
# Frames for the Application
main_frame = Frame(root, width=width_, height=height_) # Main Window
input_frame = Frame(root, width=width_, height=height_) # Take Equation from user Frame
# methods_frame = Frame(root, width=width_, height=height_) # Methods Frame
global radio_choice_frame
radio_choice_frame = Frame(input_frame)

main_frame.pack() # Show Welcome Window on Screen

round_label = Label(input_frame, text="Round to", font=("Helvetica", 12)).place(x=300, y=340)
global round_entry_value
round_entry_value = IntVar(value=1)
round_entry = Entry(input_frame, textvariable=round_entry_value, font=("Helvetica", 12), width=6).place(x=302, y=373)


max_iterations_label = Label(input_frame, text="Max Iterations", font=("Helvetica", 12)).place(x=300, y=410)

max_iterations_temp = StringVar(value=1)
max_iterations_entry = Entry(input_frame, textvariable=max_iterations_temp,
                             font=("Helvetica", 12), width=6).place(x=302, y=440)



# Menu Bar
main_menu = Menu(root)
root.config(menu=main_menu)

## File
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
# Sub-menu in help menu
file_menu.add_command(label="Exit", command=root.destroy)


## Help
help_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Help", menu=help_menu)
# Sub-menu in help menu
help_menu.add_command(label="Equation Examples", command=show_equation_examples)
help_menu.add_command(label="Input Functions", command=show_input_examples)

# Create an Entry widget
var = StringVar(value="e.g. -2+7x-5x^2+6x^3")
msg_label = Label(input_frame, text="Equation", font=("Helvetica", 16)).place(x=77, y=5)
entry = Entry(input_frame, width=50, textvariable=var,font=("Helvetica", 16))
entry.pack(pady=5)

# Add a label widget in the frame
label = Label(input_frame)
label.pack()

# Define the figure size and plot the figure
fig = matplotlib.figure.Figure(figsize=(15, 1), dpi=100)

wx = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

# Set the visibility of the Canvas figure
wx.get_xaxis().set_visible(False)
wx.get_yaxis().set_visible(False)

root.bind('<Return>', graph)

# Radio Buttons to choose methods
# List of tuples of the values and variables
# Make a frame to put radio buttons in it
radio_frame = LabelFrame(input_frame, text="Choose a Method...", padx=10, pady=10, font=("Helvetica", 12)) # Inside of the frame padding
radio_frame.pack(padx=120, pady=10, anchor=W) # Outside of the frame padding

methods = [
    ("Bisection", "bisection"),
    ("False Position Method", "false_pos"),
    ("Simple Fixed Point", "simple_fix"),
    ("Newton", "newton"),
    ("Secant", "secant")
]

global item
item = StringVar()
item.set("Bisection") # Default method value

for text, method in methods:
    Radiobutton(radio_frame, text=text, variable=item, value=method,
                command=lambda: radio_button_pressed(item.get())).pack(anchor=W)

error_label = Label(input_frame, text="Error %", font=("Helvetica", 12)).pack(padx=120, pady=10, anchor=W)
error_value = StringVar()
error_entry = Entry(input_frame, textvariable=error_value, width=10, font=("Helvetica", 12)).pack(padx=120, anchor=W)

# global error
# error = error_value.get()

xl_value = StringVar()
xu_value = StringVar()
x_value = StringVar()
xi_minus1_value = StringVar()
xi_value = StringVar()

# Images
bg_image = PhotoImage(file="./images/bg2.png")
proceed_image = PhotoImage(file="./images/proceed_button2_smaller.png")
back_image = PhotoImage(file="./images/back_button2_smaller.png")
calculate_image = PhotoImage(file="./images/calculate_button1_smaller1.png")


# Canvas
# Main Canvas
canvas_main = Canvas(main_frame, width=width_, height=height_)
canvas_main.pack(fill="both", expand=True)

# Background Image in canvas
canvas_main.create_image(0,0, image=bg_image, anchor="nw") # anchor = North West

# Label (475, 50) those are the positions of x and y
# canvas_main.create_text(width_/2, 50, text="Welcome to Equaveler!", font=("Helvetica", 50), fill="orange")
# canvas_main.create_text(width_/2, 600, text="Save your time by a click!", font=("Helvetica", 35), fill="black")

# Buttons
# Main Screen Button
proceed_button_main = Button(main_frame, activebackground="white", borderwidth=0, image=proceed_image, bg="white", command=change_to_input_frame)
proceed_button_window = canvas_main.create_window(880, 565, anchor="nw", window=proceed_button_main, width=60, height=60)


# Methods Screen Buttons
# proceed_button = Button(input_frame, borderwidth=0, image=proceed_image, command=change_to_methods_frame)
# proceed_button.place(x=880, y=570, width=60, height=60)

back_button = Button(input_frame, borderwidth=0, image=back_image, command=change_to_main_frame)
back_button.place(x=10, y=565, width=60, height=60)

choice = None
calculate_button = Button(input_frame, image=calculate_image, borderwidth=0, command=lambda: calculate_method())
calculate_button.place(x=(width_/2)-80, y=550, width=190, height=60)

# # White-Dark Theme
# button_mode=True
# def customize():
#     global button_mode
#     if button_mode:
#         theme_button.config(image=off,bg="#26242f",activebackground="#26242f")
#         input_frame.config(bg="#26242f")
#         button_mode=False
#     else:
#         theme_button.config(image=on,bg="white",activebackground="white")
#         input_frame.config(bg="white")
#         button_mode=True
        
# on = PhotoImage(file="images/light.png")
# off = PhotoImage(file="images/dark.png")
# theme_button = Button(input_frame, image=on, bd=0, bg="white", activebackground="white", command=customize)
# theme_button.pack(padx=50,pady=50)

root.mainloop()

