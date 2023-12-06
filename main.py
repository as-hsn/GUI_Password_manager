from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ("Georgia", 14)
FONT_NAME = "Georgia"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]

    symbol = [choice(symbols) for _ in range(randint(2, 4))]

    number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter + symbol + number

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web_data = web_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    json_data = {
         web_data: {
        "Email": email_data,
        "Password": password_data }
    }

    if len (web_data) == 0 or len (password_data) == 0:
        messagebox.showwarning(title="Check out fields" ,message="Please dont empty check all fields")

    else:
        is_ok = messagebox.askokcancel(title=web_data, message=f"Do you want to save your details\nEmail :{email_data}\nPassword : {password_data}")

        if is_ok:
            try:
                with open("images and data/Data.json", mode="r") as data_file:
                  load = json.load(data_file)
                  load.update(json_data)
            except FileNotFoundError:
                with open ("images and data/Data.json", mode="w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            else:
                with open ("images and data/Data.json", mode="w") as data_file:
                    json.dump(load, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)
                web_entry.focus()
#-------------------------------Searching functionallity ------------------------ #
def searching_data():

    web = web_entry.get()
    try:
        with open ("images and data/Data.json", mode="r") as data_file :
            load = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="The file name you entered does not exist")
    else:
        if web in load:
            email = load[web]["Email"]
            password = load[web]["Password"]
            messagebox.showinfo(title=web, message=f"Email : {email} \n Password : {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No data {web} exists")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
icon_image = PhotoImage(file="images and data/icon_image.png")
window.iconphoto(True, icon_image)
window.config(padx=50, pady=20)
window.title("Password Manager")
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="images and data/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#Webite Label
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0)

#Email Username Label
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

#Password label
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

#Website textbox
web_entry = Entry(width=32)
web_entry.grid(row=1, column=1)
web_entry.focus()

#Email textbox
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Hassan@gmail.com")

#Password textbox
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#Search button

search_button = Button(text="Search", font=(FONT_NAME, 10), width=13, border=0.5, command=searching_data)
search_button.grid(row=1, column=2)

#Generate button
generate_button = Button(text="Generate Password", font=(FONT_NAME, 10), border=0.5, width=14, command=gen_pass)
generate_button.grid(row=3, column=2)

#Add Button
add_button = Button(text="Add", font=(FONT_NAME, 10), width=39, border=0.5, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()