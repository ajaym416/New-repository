import tkinter as tk
import tkinter.messagebox

sk = tk.Tk( )
sk.title("Tic Tac Toe")

click = True


def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        print("pressed")
        click = False
        checkwin()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        checkwin()

def checkwin():
    if ((button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X") or
          (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X") or
          (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X") or
          (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X") or
          (button3["text"] == "X" and button5["text"] == "X" and button9["text"] == "X") or
          (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X") or
          (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X") or
          (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X")):
                tk.messagebox.showinfo("Winner X ", "You won the game")
    # shift + alt + mouse hover to select the whole column and edit
    if ((button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O") or
          (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O") or
          (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O") or
          (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O") or
          (button3["text"] == "O" and button5["text"] == "O" and button9["text"] == "O") or
          (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O") or
          (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O") or
          (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O")):
                tk.messagebox.showinfo("Winner O ", "You won the game")


buttons = tk.StringVar()

button1 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button1))
button1.grid(row=0, column=0, sticky="nsew")

button2 = tk.Button(sk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda: checker(button2))
button2.grid(row=0, column=1, sticky="nsew")

button3 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button3))
button3.grid(row=0, column=2, sticky="nsew")

button4 = tk.Button(sk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda: checker(button4))
button4.grid(row=1, column=0, sticky="nsew")

button5 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button5))
button5.grid(row=1, column=1, sticky="nsew")

button6 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button6))
button6.grid(row=1, column=2, sticky="nsew")

button7 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button7))
button7.grid(row=2, column=0, sticky="nsew")

button8 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button8))
button8.grid(row=2, column=1, sticky="nsew")

button9 = tk.Button(sk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: checker(button9))
button9.grid(row=2, column=2, sticky="nsew")

sk.mainloop()
