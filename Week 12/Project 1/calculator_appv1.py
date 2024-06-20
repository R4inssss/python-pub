import tkinter as tk
from tkinter import messagebox
import calculator_appv2


# ------------------------------- Main ------------------------------- #

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Statistics Calculator')
        self.geometry('400x600')

        self.expression = ""
        self.entry = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=5)

        self.calc_btn()

    def calc_btn(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(self, text=text, padx=20, pady=20, font=('Arial', 18),
                               command=lambda t=text: self.on_btn_click(t))
            # TODO: Create on button clicked function
            # button orientation to cardinal directions
            button.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    #            row += 1 # future planning for my functions

    # ------------------------------- Functions ------------------------------- #

    def on_btn_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)


# ------------------------------- Call ------------------------------- #


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
