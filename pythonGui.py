import tkinter as tk

firstNumber = 0
secondNumber = 0
equation = "0"
operation = ""

def ResetAll() :
    global equation,firstNumber,operation,secondNumber
    firstNumber = 0
    secondNumber = 0
    equation = "0"
    operation = ""
    UpdateScreen()

def Evaluate() :
    global operation,equation,secondNumber
    if operation != "":
        secondNumber = int(equation)
        equation = str(Calculate())
        UpdateScreen()

def Calculate() :
    global equation,firstNumber,operation,secondNumber
    result = 0
    if not operation == "":
        if operation == "+":
            result = firstNumber + secondNumber
        elif operation == "-":
            result = firstNumber - secondNumber
        elif operation == "*":
            result = firstNumber*secondNumber
        else:
            result = firstNumber/secondNumber
        ResetAll()
        print(str(result)) 
        return result
s

def callback():
    print("hello")
    return

def UpdateTextField() :
    text_field.config(state=tk.NORMAL)
    text_field.insert(tk.END,"siema")
    text_field.config(state=tk.DISABLED)

def NextDigit(n) :
    global equation
    if (int(equation)<10000000) :
        if(equation == "0") :
            equation = ""
        equation = equation + str(n)
    UpdateScreen()

def ClearText() :
    text_field.delete(1.0,tk.END)

def UpdateScreen() :
    text_field.config(state=tk.NORMAL)
    ClearText()
    text_field.insert(tk.END,equation)
    text_field.config(state=tk.DISABLED)

def SetOperation(n) :
    global equation,operation,firstNumber
    if operation == "":
        firstNumber = int(equation)
        equation = "0"
        operation = n
        UpdateScreen()
mainWindow = tk.Tk()

mainWindow.title("Calculator")

text_field = tk.Text(mainWindow, height=1, width=12)
text_field.pack()
text_field.insert(tk.END, equation)
text_field.config(state=tk.DISABLED)

testFrame = tk.Frame(mainWindow)

button1 = tk.Button(testFrame,text = "1", command = lambda: NextDigit(1))
button2 = tk.Button(testFrame,text = "2", command = lambda: NextDigit(2))
button3 = tk.Button(testFrame,text = "3", command = lambda: NextDigit(3))
button4 = tk.Button(testFrame,text = "4", command = lambda: NextDigit(4))
button5 = tk.Button(testFrame,text = "5", command = lambda: NextDigit(5))
button6 = tk.Button(testFrame,text = "6", command = lambda: NextDigit(6))
button7 = tk.Button(testFrame,text = "7", command = lambda: NextDigit(7))
button8 = tk.Button(testFrame,text = "8", command = lambda: NextDigit(8))
button9 = tk.Button(testFrame,text = "9", command = lambda: NextDigit(9))
button0 = tk.Button(testFrame,text = "0", command = lambda: NextDigit(0))
buttonPlus = tk.Button(testFrame,text = "+", command = lambda: SetOperation("+"))
buttonMinus = tk.Button(testFrame,text = "-", command = lambda: SetOperation("-"))
buttonClear = tk.Button(testFrame,text = "C", command = lambda: ResetAll())
buttonMul = tk.Button(testFrame,text = "*", command = lambda: SetOperation("*"))
buttonDiv = tk.Button(testFrame,text = "/", command = lambda: SetOperation("\\"))
buttonSum = tk.Button(testFrame,text = "=", command = lambda: Evaluate())
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=0,column=0)
button8.grid(row=0,column=1)
button9.grid(row=0,column=2)
buttonPlus.grid(row=3,column=0)
button0.grid(row=3,column=1)
buttonMinus.grid(row=3,column=2)
buttonMul.grid(row=0,column=3)
buttonDiv.grid(row=1,column=3)
buttonClear.grid(row=2,column = 3)
buttonSum.grid(row=3,column=3)
text_field.pack(side=tk.TOP)

testFrame.pack(side=tk.TOP)
mainWindow.geometry("200x150")
mainWindow.resizable(False,False)
mainWindow.mainloop()