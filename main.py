from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def find_it():
    website=web_info.get()
    with open("password.json","r") as file:
        data=json.load(file)
    # print(data[website])
    messagebox.showinfo(title=website,message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")

def password_genertor():

    password_info.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = [random.choice(symbols) for _ in range(nr_symbols)] + password_list # add list with list
    password_list = [random.choice(numbers) for _ in range(nr_numbers)] + password_list
    random.shuffle(password_list)
    passwo = "".join(password_list)


    password_info.insert(0, passwo)
    pyperclip.copy(passwo)
    messagebox.showinfo(title="copied", message="your password is succesfuly copy to the clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def addtofile():
    website = web_info.get()
    emailll = email_info.get()
    passwords = password_info.get()
    new_data = {
        website: {
            "email": emailll,
            "password": passwords
        }
    }
    if len(website) == 0 or len(emailll) == 0 or len(passwords) == 0:
        messagebox.showwarning(title="oops", message="please don't leave empty fields")
    else:
        responce = messagebox.askokcancel(title=web_info.get(),
                                          message=f"The detail you entered\n Website: {web_info.get()}\nEmail: {email_info.get()}\npassword: {password_info.get()}\nis it ok to save?")
        if responce:
            def jc_ubdate():
                with open("password.json","w") as neee:
                    json.dump(new_data,neee,indent=4)

            try:
                with open("password.json", "r") as ppp:
                    #reading_old
                    # json.update(new_data, ppp, indent=4)
                    # if ppp.read()!="":
                    data=json.load(ppp)
                    # like updata in dict
                    new_data.update(data)
            except FileNotFoundError:
                jc_ubdate()
            else:
                jc_ubdate()
            finally:
                web_info.delete(0, END)
                password_info.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")

window.config(padx=50, pady=50)

canva = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file="logo.png")
c = canva.create_image(100, 100, image=lock)
canva.grid(row=0, column=1)

web = Label(text="Website:", padx=15)
web.grid(row=1, column=0)

web_info = Entry(width=30)
web_info.focus()
# webisite=web_info.get()
web_info.grid(row=1, column=1)

search=Button(text="search",command=find_it)
search.grid(row=1,column=2)

emai = Label(text="Email/username:", padx=15, pady=10)
emai.grid(row=2, column=0)

email_info = Entry(width=45)
email_info.insert(0, "gopikarthik173@gmail.com")
# ema=email_info.get()
email_info.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", padx=15, pady=10)
password.grid(row=3, column=0)

password_info = Entry(width=27)
# passs=password_info.get()
password_info.grid(row=3, column=1)

gen = Button(text="generate password", bg="white", command=password_genertor)
gen.grid(row=3, column=2)

ad = Button(text="Add", width=39, bg="white", command=addtofile)
ad.grid(row=4, column=1, columnspan=2)

window.mainloop()
