import tkinter
# intit
root = tkinter.Tk()
root.title("Calculator")
root.geometry("570x650")
entry = tkinter.Entry(root, width=20, font=("Arial", 18))
entry.pack(pady=15)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
currentmode = "light"


currentbuttonmode = "light"

def buttoncolor(buttons, mode):
    for button in buttons:
        if mode == "dark":
            button.config(bg="grey", fg="white")
        else:
            button.config(bg="white", fg="black")


def changebg():
    global currentmode
    #begin
    if currentmode == "light":
        currentmode = "dark"
        root.config(bg="black")
        buttoncolor(buttons, "dark")

        entry.config(bg="black", fg="white")

    else:
        currentmode == "dark"
        currentmode = "light"
        root.config(bg="white")

        entry.config(bg="white", fg="white")
        buttoncolor(buttons, "white")

        # change button colors


# Initialize currentinput as an empty string
currentinput = ""



def clearentry():
    global currentinput
    currentinput = ""
    entry.delete(0, tkinter.END)

# Function to append numbers to the current input
def getnumber(number):
    global currentinput
    # Add the number to the current input string
    print(currentinput)
    currentinput += str(number)
    # Update the entry with the new input
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, currentinput)

# Function to add "+" to the current input



def subtractnumber():
    global currentinput
    currentinput += " - "
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, currentinput)


def dividenumber():
    global currentinput
    currentinput += " / "
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, currentinput)
def multiplynumber():
    global currentinput
    currentinput += " x "
    entry.delete(0 , tkinter.END)
    entry.insert(tkinter.END, currentinput)

def addnumber():
    global currentinput
    currentinput += " + "
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, currentinput)

# Function to evaluate the expression when "=" is pressed




def evaluate():
    global currentinput
    try:
        expression = currentinput.replace("÷", "/")
        expression = currentinput.replace("x", "*")
        result = eval(expression)  # Evaluate the current input string
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, str(result))
        currentinput = str(result)  # Save the result for further calculations
    except Exception:
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, "Error")
        currentinput = ""







# Create number buttons and place them
one = tkinter.Button(root, text="1",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(1))
one.place(x=0, y=325)

two = tkinter.Button(root, text="2",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(2))
two.place(x=115, y=325)

three = tkinter.Button(root, text="3",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(3))
three.place(x=230, y=325)

four = tkinter.Button(root, text="4",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(4))
four.place(x=345, y=325)

five = tkinter.Button(root, text="5",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(5))
five.place(x=460, y=325)




six = tkinter.Button(root, text="6",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(6))
six.place(x=0, y=485)



seven = tkinter.Button(root, text="7",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(7))
seven.place(x=115, y=485)



eight = tkinter.Button(root, text="8",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(8))
eight.place(x=230, y=485)



nine = tkinter.Button(root, text="9",font=("Arial", 15), width=15, height=10, command=lambda: getnumber(9))
nine.place(x=345, y=485)

zero = tkinter.Button(root, text="0", font=("Arial", 15),width=15, height=10, command=lambda: getnumber(0))
zero.place(x=460, y=485)




# Create the "+" button
addbutton = tkinter.Button(root, text="+", width=15, height=5,command=lambda: addnumber())
addbutton.place(x=460, y=80)


multiplybutton = tkinter.Button(root, text="x", width=15, height=5, command=lambda: multiplynumber())
multiplybutton.place(x=460, y=165)


dividebutton = tkinter.Button(root, text="÷", width=15, height=5, command=dividenumber)
dividebutton.place(x=345, y=87)

# Create an "=" button to evaluate the expression
equalsbutton = tkinter.Button(root, text="=", width=15, height=5, command=evaluate)
equalsbutton.place(x=460, y=0)

subtractionbutton = tkinter.Button(root, text="-", width=15, height=5, command=subtractnumber)
subtractionbutton.place(x=345, y=170)

clearbutton = tkinter.Button(root, text="Clear", width=5, height=5, command=clearentry)
clearbutton.place(x=420)



changebgcolorbutton = tkinter.Button(root, text="CHANGE MODE", width=15, height=2, command=lambda: changebg())
changebgcolorbutton.place(x=0)



buttons = [one, two, three, four, five, six, seven, eight, nine, zero, addbutton, subtractionbutton, clearbutton, dividebutton, multiplybutton, equalsbutton]







# Start the main loop






root.mainloop()

