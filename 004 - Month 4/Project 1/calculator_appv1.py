import tkinter as tk
from tkinter import messagebox
import statisticsProgramv7


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
            # button orientation to cardinal directions
            button.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Statistics Button GUI and call
        stats_btn = tk.Button(self, text='Statistics', padx=20, pady=20, font=('Arial', 18),
                              command=self.open_statistics_menu)
        stats_btn.grid(row=row, column=0, columnspan=4, sticky="nsew")

        row += 1  # There's probably a better way to make a new row, but I don't know how to yet :)

        # Clear button GUI and call
        clr_btn = tk.Button(self, text='Clear', padx=20, pady=20, font=('Arial', 18),
                            command=self.clr_button)
        clr_btn.grid(row=row, column=0, columnspan=4, sticky="nsew")

    # ------------------------------- Functions ------------------------------- #

    # Function 1, event handler for input
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

    # Function 2, statistics button and menu
    def open_statistics_menu(self):
        stats_window = tk.Toplevel(self)
        stats_window.title('Statistics')
        stats_window.geometry('400x600')

    # Function 3, clear button
    def clr_button(self):
        self.expression = ""
        self.entry.delete(0, tk.END)


# ------------------------------- Call ------------------------------- #


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
