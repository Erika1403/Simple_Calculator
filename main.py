import tkinter
import numpy

window = tkinter.Tk()

window.title("PyCalculator")
window.maxsize(width=420, height=540)
window.configure(background='white')
acolor = '#d13732'
norcolor = 'gray'
aforcolor = 'white'
upbgcolor = '#bab8b3'
fgcolor = 'black'
upbuttonlabels = ['C', 'Del', '%', '/']
otherbuttonlbl = numpy.array([['7', '8', '9', 'x'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], [' ', '0', '.', '=']])
tocompute = []


# Functions
def compute(eq):
    try:
        result = eval(eq)
        tocompute.clear()
        res = str(result)
        if len(res) > 10:
            return str(round(result, 2))
        else:
            return res

    except Exception as e:
        return "Error"


def write(num):
    curr_equation = lblResult['text']
    if num == '=':
        equation = str(curr_equation)
        tocompute.append(equation)
        lblResult.config(text=compute(''.join(tocompute)))
    elif num == '+' or num == '-' or num == '/' or num == 'x':
        equation = str(curr_equation)
        tocompute.append(equation)
        if num == 'x':
            tocompute.append('*')
        else:
            tocompute.append(num)
        lblResult.config(text='')
    elif num == '%':
        res = float(curr_equation)/100
        lblResult.config(text=str(res))
    elif num == 'C':
        tocompute.clear()
        lblResult.config(text='')
    elif num == 'Del':
        equation = str(curr_equation)
        lblResult.config(text=equation[:-1])
    else:
        equation = str(curr_equation) + str(num)
        lblResult.config(text=equation)


# Label
lblResult = tkinter.Label(window, text='', bg='white', fg='black')
lblResult.grid(row=0, column=0, columnspan=5, pady=(25, 25), sticky='w')
lblResult.config(font=('verdana', 30, 'bold'))
col = 0
# Buttons
for btn in upbuttonlabels:
    new_btn = tkinter.Button(window, text=btn, bg=upbgcolor, fg=fgcolor, width=5, height=2, activebackground=acolor,
                             activeforeground=aforcolor, command=lambda btn=btn: write(btn))
    new_btn.grid(row=1, column=col)
    new_btn.config(font=('verdana', 20, 'bold'))
    col = col + 1

col = 0
r = 2
rows = 0
for buttons in otherbuttonlbl:
    for btn in buttons:
        if col > 3:
            col = 0
            r = r + 1
        ope = otherbuttonlbl[rows, col]
        new_btn = tkinter.Button(window, text=ope, bg=norcolor, fg=fgcolor, width=5, height=2, activebackground=acolor,
                                 activeforeground=aforcolor, command=lambda ope=ope: write(ope))
        new_btn.grid(row=r, column=col)
        new_btn.config(font=('verdana', 20, 'bold'))
        col = col + 1

    rows = rows + 1

window.mainloop()
