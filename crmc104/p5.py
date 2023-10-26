import tkinter as tk


def calculate_total():
    mark1 = float(entry_test1.get())
    mark2 = float(entry_test2.get())
    total = mark1 + mark2
    label_result.config(text=f"{total}")


window = tk.Tk()
window.title("Mark Calculator")
# Create and organize widgets using the grid manager
label_test1 = tk.Label(window, text="Enter Test 1 Mark:")
label_test1.grid(row=0, column=0)
entry_test1 = tk.Entry(window)
entry_test1.grid(row=0, column=1)
label_test2 = tk.Label(window, text="Enter Test 2 Mark:")
label_test2.grid(row=1, column=0)
entry_test2 = tk.Entry(window)
entry_test2.grid(row=1, column=1)
calculate_button = tk.Button(
    window, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=2, column=0)
label_result = tk.Label(window)
label_result.grid(row=2, column=1)
window.mainloop()
