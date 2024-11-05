import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

password = str()
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []


def generate_password():
    global password, password_list

    if length_entry.get():
        length = int(length_entry.get())
    else:
        messagebox.showwarning("Error", "You must provide the length of the password")
        return
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    if use_uppercase:
        password_list += [random.choice(string.ascii_uppercase) for each in range(6)]
    if use_lowercase:
        password_list += [random.choice(string.ascii_lowercase) for each in range(6)]
    if use_numbers:
        password_list += [random.choice(string.digits) for each in range(6)]
    if use_symbols:
        password_list += [random.choice(symbols) for each in range(6)]
    password = "".join(random.choice(password_list) for _ in range(length))
    password_label.config(text=f"Your password is : {password}", pady=10)


def copy_to_clipboard():
    global password
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")
    length_entry.delete(0, END)


# Set up the GUI window
window = Tk()
window.title("Secure Password Generator")
window.config(padx=200, pady=80, background="#43766C")

Label(text="Password Length:", pady=10, background="#43766C", font=20).grid(row=0, column=0)
length_entry = Entry()
length_entry.grid(row=0, column=1)

uppercase_var = BooleanVar()
lowercase_var = BooleanVar()
numbers_var = BooleanVar()
symbols_var = BooleanVar()

Checkbutton(text="Include Uppercase", variable=uppercase_var, background="#43766C", font=4).grid(row=1, column=0,
                                                                                                 columnspan=2)
Checkbutton(text="Include Lowercase", variable=lowercase_var, background="#43766C", font=4).grid(row=2, column=0,
                                                                                                 columnspan=2)
Checkbutton(text="Include Numbers", variable=numbers_var, background="#43766C", font=4).grid(row=3, column=0,
                                                                                             columnspan=2)
Checkbutton(text="Include Symbols", variable=symbols_var, background="#43766C", font=4).grid(row=4, column=0,
                                                                                             columnspan=2)

Button(text="Generate Password", command=generate_password, background="#E1AA74", font=4).grid(row=5, column=0,
                                                                                               columnspan=2)
password_label = Label(background="#43766C", font=20)
password_label.grid(row=6, column=0, columnspan=2)

Button(text="Copy to Clipboard", command=copy_to_clipboard, background="#E1AA74", font=4).grid(row=7, column=0,
                                                                                               columnspan=2)

window.mainloop()
