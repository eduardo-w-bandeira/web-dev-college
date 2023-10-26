import tkinter as tk


def calculate_sum():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    result_label.config(text=f"Sum: {result}")


window = tk.Tk()
window.title("Sum Calculator")
label_num1 = tk.Label(window, text="Enter Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1)
label_num2 = tk.Label(window, text="Enter Number 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1)
calculate_button = tk.Button(
    window, text="Calculate Sum", command=calculate_sum)
calculate_button.grid(row=2, column=0)
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=1)
window.mainloop()
