import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Простой калькулятор")
        self.window.geometry("250x350")
        
        self.current_input = ""
        self.result_var = tk.StringVar()
        
        self.create_interface()
    
    def create_interface(self):
       
        result_frame = tk.Frame(self.window)
        result_frame.pack(pady=10)
        
        result_label = tk.Label(result_frame, textvariable=self.result_var, 
                               font=('Arial', 18), bg='white', width=15, height=2, relief='sunken')
        result_label.pack(padx=10, pady=10)
        
        digits_frame = tk.Frame(self.window)
        digits_frame.pack()
        
        digits = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', 'C']
        ]
        
        for i, row in enumerate(digits):
            for j, digit in enumerate(row):
                if digit == 'C':
                    btn = tk.Button(digits_frame, text=digit, font=('Arial', 14),
                                   command=self.clear, width=5, height=2, bg='red', fg='white')
                else:
                    btn = tk.Button(digits_frame, text=digit, font=('Arial', 14),
                                   command=lambda x=digit: self.add_digit(x), width=5, height=2)
                btn.grid(row=i, column=j, padx=2, pady=2)
        
     
        operations_frame = tk.Frame(self.window)
        operations_frame.pack(pady=10)
        
        operations = ['+', '-', '*', '=']
        
        for i, op in enumerate(operations):
            if op == '=':
                btn = tk.Button(operations_frame, text=op, font=('Arial', 14),
                               command=self.calculate, width=5, height=2, bg='lightgreen')
            else:
                btn = tk.Button(operations_frame, text=op, font=('Arial', 14),
                               command=lambda x=op: self.add_operation(x), width=5, height=2)
            btn.grid(row=0, column=i, padx=2, pady=2)
    
    def add_digit(self, digit):
        self.current_input += digit
        self.result_var.set(self.current_input)
    
    def add_operation(self, operation):
        if self.current_input and self.current_input[-1] not in ['+', '-', '*']:
            self.current_input += operation
            self.result_var.set(self.current_input)
    
    def clear(self):
        self.current_input = ""
        self.result_var.set("")
    
    def calculate(self):
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
            self.result_var.set(self.current_input)
        except:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            self.clear()
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = SimpleCalculator()
    calc.run()