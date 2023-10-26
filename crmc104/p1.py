import tkinter as tk


def display_message():
    name = entry_name.get()
    age = entry_age.get()
    welcome_label.config(text=f"Welcome, {name}! You are {age}")


window = tk.Tk()
window.title("Welcome Message App")
label_name = tk.Label(window, text="Enter your name:")
entry_name = tk.Entry(window)
label_age = tk.Label(window, text="Enter your age:")
entry_age = tk.Entry(window)
welcome_button = tk.Button(
    window, text="Show Welcome Message", command=display_message)
label_name.pack()
entry_name.pack()
label_age.pack()
entry_age.pack()
welcome_button.pack()
welcome_label = tk.Label(window, text="")
welcome_label.pack()
window.mainloop()
