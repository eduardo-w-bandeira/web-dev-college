import tkinter as tk


def calculate_sum():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    num3 = float(entry_num3.get())
    total = num1 + num2 + num3
    avg = total / 3
    result_label.config(text=f"Total marks: {total}")
    avg_label.config(text=f"Average Marks: {avg}")


window = tk.Tk()
window.title("Student Mark Calculator")
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
    window, text="Calculate Total and Average", command=calculate_sum)
calculate_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
avg_label = tk.Label(window, text="")
avg_label.pack()
window.mainloop()
