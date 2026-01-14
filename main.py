from tkinter import *
from tkinter import messagebox
from passwordGenerator import generate_password
import pyperclip

def save():
   website = website_entry.get()
   email = email_entry.get()
   password = password_entry.get()

   is_ok = messagebox.askokcancel(title=website , message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs this ok to save?")

   if len(website) == 0 or len(password) == 0:
      messagebox.showinfo(title="Oops" , detail="Please fill all the fields")

   else:
      if is_ok:
         with open('data.txt' , 'a') as data_file:
            data_file.write(f'{website} | {email} | {password}\n')
            website_entry.delete(0,END)
            password_entry.delete(0,END)
   
def generate():

   password = generate_password()
   password_entry.delete(0 , END)
   password_entry.insert(0 , password)
   pyperclip.copy(password)


window = Tk()
window.title("Password Mnager")
window.config(padx=20 , pady=20)

canvas = Canvas(height=200 , width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image = logo)
canvas.grid(row = 0 , column=1)

webstie_label = Label(text = "Website")
webstie_label.grid(row=1,column=0)
email_label = Label(text="Email/UserName")
email_label.grid(row=2 ,column=0)
password_label = Label(text="Password" , )
password_label.grid(row=3 , column=0)

website_entry = Entry()
website_entry.grid(row=1 , column=1 , columnspan=2)
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2 , column=1 , columnspan=2)
email_entry.insert(0, "test")
password_entry = Entry()
password_entry.grid(row =3 , column=1 , columnspan=2)

gernerate_button = Button(text="Generate button" , command=generate)
gernerate_button.grid(row=3 , column=2 , columnspan=2)
add_buton = Button(text = "Add" , width=16 , command=save )
add_buton.grid(row=4 , column=1)
add_buton.config(padx=1 , pady=0)



window.mainloop()


