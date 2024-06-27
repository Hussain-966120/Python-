import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + number)

def button_clear():
    entry_var.set("")

def button_equal():
    expression = entry_var.get()
    try:
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

entry_var = tk.StringVar()
entry_var.set("")
entry = tk.Entry(window, textvariable=entry_var, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_bg = "#f0f0f0"
button_fg = "#333333"
button_active_bg = "#dddddd"

tk.Button(window, text='7', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('7')).grid(row=1, column=0)
tk.Button(window, text='8', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('8')).grid(row=1, column=1)
tk.Button(window, text='9', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('9')).grid(row=1, column=2)
tk.Button(window, text='/', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('/')).grid(row=1, column=3)

tk.Button(window, text='4', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('4')).grid(row=2, column=0)
tk.Button(window, text='5', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('5')).grid(row=2, column=1)
tk.Button(window, text='6', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('6')).grid(row=2, column=2)
tk.Button(window, text='*', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('*')).grid(row=2, column=3)

tk.Button(window, text='1', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('1')).grid(row=3, column=0)
tk.Button(window, text='2', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('2')).grid(row=3, column=1)
tk.Button(window, text='3', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('3')).grid(row=3, column=2)
tk.Button(window, text='-', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('-')).grid(row=3, column=3)

tk.Button(window, text='0', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('0')).grid(row=4, column=0)
tk.Button(window, text='C', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=button_clear).grid(row=4, column=1)
tk.Button(window, text='=', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=button_equal).grid(row=4, column=2)
tk.Button(window, text='+', padx=40, pady=20, bg=button_bg, fg=button_fg, activebackground=button_active_bg,
          command=lambda: button_click('+')).grid(row=4, column=3)

window.mainloop()
