from bf import run_brainfuck

import tkinter as tk
from functools import partial   

def execute_bf():
    code = code_entry.get("1.0", "end-1c")
    user_input = user_input_entry.get()
    output = run_brainfuck(code, user_input)
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)  
    output_text.insert(tk.END, output) 
    output_text.config(state=tk.DISABLED) 

def clear():
    code_entry.delete("1.0", tk.END)  
    output_text.config(state=tk.NORMAL)  
    output_text.delete("1.0", tk.END)  
    output_text.config(state=tk.DISABLED)  
    user_input_entry.delete(0, tk.END)

window = tk.Tk()
window.geometry("700x500")
window.title("Brainfuck Interpreter")

# Input field for bf code
code_label = tk.Label(window, text="Enter Brainfuck code:")
code_label.pack()
code_entry = tk.Text(window, height = 10, width=50) 
code_entry.pack(ipady=10)



# Input field for user input
user_input_label = tk.Label(window, text="Enter user input (if needed):")
user_input_label.pack()
user_input_entry = tk.Entry(window)
user_input_entry.pack()

# Execute button
execute_button = tk.Button(window, text="Execute", command=execute_bf)
execute_button.pack()

# Output field
output_label = tk.Label(window, text="Output:")
output_label.pack()
output_text = tk.Text(window, height=10, width=50)
output_text.pack()
output_text.config(state=tk.DISABLED)  # Initially disable editing of the output text

# Clear button
clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.pack()


window.mainloop()