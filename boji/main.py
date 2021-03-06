from tkinter import *
from PIL import Image, ImageTk
import os

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =delete2).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.configure(bg="#696969")
  screen.title("Notes 1.0")
  Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()


  image_bg=ImageTk.PhotoImage(file='images/login.png')
  # creating label for image
  lable=Label(screen, bd=0, relief="sunken", bg="#696969")
  lable.place(x=20,y=50)
  lable.config(image=image_bg)
  
  image_bg1=ImageTk.PhotoImage(file='images/page.png')
  # creating label for image
  lable1=Label(screen, bd=0, relief="sunken", bg="#696969")
  lable1.place(x=220,y=60)
  lable1.config(image=image_bg1)

  
  btn_inactive = Image.open("images/login_norm.png")
  btn_active = Image.open("images/login_hover.png")

  screen.btn_inactive =  ImageTk.PhotoImage(btn_inactive)
  screen.btn_active =  ImageTk.PhotoImage(btn_active)

  def on_enter(event):
    login_btn.config(image=screen.btn_active)

  def on_leave(event):
    login_btn.config(image=screen.btn_inactive)

  login_btn=Button(screen, image=screen.btn_inactive, bg="#696969", width=90, height=50, bd=0, relief="sunken", activebackground="#696969", command=login)
  login_btn.place(x=102,y=90)

  

  login_btn.bind("<Enter>", on_enter)
  login_btn.bind("<Leave>", on_leave)
  #---------------------------------------#

  btn_inactive1 = Image.open("images/register_norm.png")
  btn_active1 = Image.open("images/register_hover.png")

  screen.btn_inactive1 =  ImageTk.PhotoImage(btn_inactive1)
  screen.btn_active1 =  ImageTk.PhotoImage(btn_active1)

  def on_enter(event):
    register_btn.config(image=screen.btn_active1)

  def on_leave(event):
    register_btn.config(image=screen.btn_inactive1)

  register_btn=Button(screen, image=screen.btn_inactive1, bg="#696969", width=120, height=50, bd=0, relief="sunken", activebackground="#696969", command=register)
  register_btn.place(x=90,y=150)

  

  register_btn.bind("<Enter>", on_enter)
  register_btn.bind("<Leave>", on_leave)
  #-----------------------------------------#



  screen.mainloop()

main_screen()

# A9A9A9 BTN gray

