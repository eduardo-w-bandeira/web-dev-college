import tkinter as tk


def calculate_sum():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    num3 = float(entry_num3.get())
    result = num1 + num2 + num3
    result_label.config(text=f"Sum: {result}")


window = tk.Tk()
window.title("Sum Calculator")
label_num1 = tk.Label(window, text="Enter Number 1:")
entry_num1 = tk.Entry(window)
label_num2 = tk.Label(window, text="Enter Number 2:")
entry_num2 = tk.Entry(window)
label_num3 = tk.Label(window, text="Enter Number 3:")
entry_num3 = tk.Entry(window)
label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
label_num3.pack()
entry_num3.pack()
calculate_button = tk.Button(
    window, text="Calculate Sum", command=calculate_sum)
calculate_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
