import tkinter as tk

def callback():
    print("hello")
    return

def UpdateTextField() :
    text_field.config(state=tk.NORMAL)
    text_field.insert(tk.END,"siema")
    text_field.config(state=tk.DISABLED)

mainWindow = tk.Tk()

mainWindow.title("Calculator")


exit_button = tk.Button(
    mainWindow,
    text= "test",
    command =lambda: UpdateTextField()
)

exit_button2 = tk.Button(
    mainWindow,
    text= "Exit",
    command =lambda: callback()
)

exit_button3 = tk.Button(
    mainWindow,
    text= "Exit",
    command =lambda: callback()
)

equation = "123"
text_field = tk.Text(mainWindow, height=1, width=12)
text_field.pack()
text_field.insert(tk.END, equation)
text_field.config(state=tk.DISABLED)

testFrame = tk.Frame(mainWindow)

button1 = tk.Button(testFrame,text = "C", command = lambda: callback())
button2 = tk.Button(testFrame,text = "2", command = lambda: callback())
button3 = tk.Button(testFrame,text = "3", command = lambda: callback())
button4 = tk.Button(testFrame,text = "4", command = lambda: callback())
button5 = tk.Button(testFrame,text = "5", command = lambda: callback())
button6 = tk.Button(testFrame,text = "6", command = lambda: callback())
button7 = tk.Button(testFrame,text = "7", command = lambda: callback())
button8 = tk.Button(testFrame,text = "8", command = lambda: callback())
button9 = tk.Button(testFrame,text = "9", command = lambda: callback())
button0 = tk.Button(testFrame,text = "0", command = lambda: callback())
buttonPlus = tk.Button(testFrame,text = "+", command = lambda: callback())
buttonMinus = tk.Button(testFrame,text = "-", command = lambda: callback())
buttonClear = tk.Button(testFrame,text = "C", command = lambda: callback())
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=0,column=0)
button8.grid(row=0,column=1)
button9.grid(row=0,column=2)
buttonClear.grid(row=3,column=0)
button0.grid(row=3,column=1)
buttonMinus.grid(row=3,column=2)

text_field.pack(side=tk.TOP)

testFrame.pack(side=tk.TOP)
mainWindow.mainloop()