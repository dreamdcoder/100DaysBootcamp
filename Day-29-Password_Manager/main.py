import random
import tkinter as tk
import tkinter.messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'attempts', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_syms = random.randint(2, 4)
    nr_nums = random.randint(2, 4)

    pwd = [ random.choice(letters) for _ in range(nr_letters)]
    pwd += [random.choice(numbers) for _ in range(nr_nums)]
    pwd += [random.choice(symbols)for _ in range(nr_syms)]

    # print(pwd)


    # for i in range(nr_letters):
    #     letter = random.choice(letters)
    #     pwd.append(letter)
    #
    # for j in range(nr_nums):
    #     number = random.choice(numbers)
    #     pwd.append(number)
    #
    # for k in range(nr_syms):
    #     symbol = random.choice(symbols)
    #     pwd.append(symbol)

    random.shuffle(pwd)
    pwd =''.join(pwd)
    # print(pwd)
    pwd_input.delete(0,tk.END)
    pwd_input.insert(0,pwd)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    user_name = user_name_input.get()
    pwd = pwd_input.get()
    if len(website) == 0 or len(user_name) == 0:
        tk.messagebox.showinfo(title="Oops", message="You have left empty fields.")
    else:
        is_ok = tk.messagebox.askokcancel(title=website,
                                          message=f"These are the details entered: \nEmail:{user_name}\nPassword:{pwd}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website}  |  {user_name}  |  {pwd}\n")
                web_input.delete(0, tk.END)
                pwd_input.delete(0, tk.END)
                web_input.focus()

    # ---------------------------- UI SETUP ------------------------------- #


BGCOLOR = "#EDEDED"

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BGCOLOR)
canvas = tk.Canvas(width=200, height=200, bg=BGCOLOR, highlightthickness=0)
canvas.grid(row=0, column=1)

logo_image = tk.PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_image)

web_label = tk.Label(text='Website:', bg=BGCOLOR)
web_label.grid(row=2, column=0)

web_input = tk.Entry(width=51)
web_input.grid(row=2, column=1, columnspan=2)
web_input.focus()

user_name_label = tk.Label(text="Email/Username:", bg=BGCOLOR)
user_name_label.grid(row=3, column=0)

user_name_input = tk.Entry(width=51)
user_name_input.grid(row=3, column=1, columnspan=2)
user_name_input.insert(0, "yogi100888@gmail.com")

pwd_label = tk.Label(text="Password:")
pwd_label.grid(row=4, column=0, columnspan=1)

pwd_input = tk.Entry(width=33)
pwd_input.grid(row=4, column=1, columnspan=1)

pwd_gen_button = tk.Button(text="Generate Password", bg=BGCOLOR,command=generate_pwd)
pwd_gen_button.grid(row=4, column=2)

Add_button = tk.Button(text="Add", bg=BGCOLOR, width=42, command=save_data)
Add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
