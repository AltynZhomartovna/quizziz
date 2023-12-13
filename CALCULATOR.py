import tkinter as tk

def on_button_click(button_text, entry):
    current_entry_text = entry.get()

    if button_text == 'C':
        entry.delete(0, tk.END)
    elif button_text == '=':
        try:
            result = eval(current_entry_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

def calcu():
    root = tk.Tk()
    root.title("Calculator")

    entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: on_button_click(t, entry))
        button.grid(row=row, column=col, sticky='nsew')

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    calcu()

