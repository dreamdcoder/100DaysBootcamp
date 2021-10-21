# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
BGCOLOR="#EDEDED"
import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg=BGCOLOR)
canvas = tk.Canvas(width=200,height=200,bg=BGCOLOR,highlightthickness=0)
canvas.grid(row=0,column=1)

logo_image = tk.PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_image)

web_label = tk.Label(text='Website:',bg=BGCOLOR)
web_label.grid(row=2,column=0)

web_input = tk.Entry(width=51)
web_input.grid(row=2,column=1,columnspan=2)


user_name_label = tk.Label(text="Email/Username:",bg=BGCOLOR)
user_name_label.grid(row=3,column=0)

user_name_input = tk.Entry(width=51)
user_name_input.grid(row=3,column=1,columnspan=2)


pwd_label = tk.Label(text="Password:")
pwd_label.grid(row=4,column=0,columnspan=1)

pwd_input = tk.Entry(width=33)
pwd_input.grid(row=4, column=1,columnspan=1)

pwd_gen_button = tk.Button(text="Generate Password",bg=BGCOLOR)
pwd_gen_button.grid(row=4,column=2)


Add_button = tk.Button(text="Add",bg=BGCOLOR,width=42)
Add_button.grid(row=5,column=1,columnspan=2)




window.mainloop()
