import tkinter as tk # import tkinter as tk 
from tkinter import messagebox # import messagebox from tkinter
import main # import main.py

# create function to define and create GUI interface
def startGUI():
    # Create window
    window = tk.Tk() 
    # set window size
    window.geometry("400x450")
    # set minimum window size
    window.minsize(400, 450)
    # set window title
    window.title("Mystify")
    # set window background colour to be a dark blue colour
    window.configure(bg="#2D2B55")

    # Create widgets for the window
    
    # create header
    header = tk.Label(text="Mystify Seed Generation", font='Helvetica 20 bold', bg="#2D2B55", fg='#FAD000') 
    # create website text
    website_direction = tk.Label(text="Head to 127.0.0.1:5000 for web interface!", font='Helvetica 13', bg="#2D2B55", fg='#FAD000')
    # Instructions for encrypting passwords using the GUI.
    input_direction = tk.Label(text="Type in the password you wish to encrypt in the input box below, then hit the encrypt button.", font='Helvetica 7', bg="#2D2B55", fg='#FAD000')
    # create input box for password
    password_input = tk.Entry(window, width=20, bg="#FAD000", fg='#2D2B55')
    # create button to encrypt password
    password_button = tk.Button(text="Encrypt", command=lambda: encrypt(password_input), bg="#FAD000", fg='#2D2B55')
    # create button to seed_button text
    seed_button = tk.Button(text="Generate Seed", command=generateSeed, bg="#FAD000", fg='#2D2B55')
    # create label with text from main.py
    text = tk.Label(text=main.main(), bg='#2D2B55', fg='#FF7200', font='Helvetica 10 bold')
    
    # Pack each widget into the window
    header.pack()
    website_direction.pack()
    input_direction.pack()
    password_input.pack()
    password_button.pack()
    seed_button.pack()
    text.pack()

    # Run window in loop until closed
    window.mainloop()
    
# create function to seed_button text on each button click, by getting the seed and displaying it into our gui
def generateSeed():
    # create label with text from main.py
    seed = tk.Label(text=main.main(), bg='#2D2B55', fg="#FF7200", font='Helvetica 10 bold')
    # pack label into window
    seed.pack()

# after encrypt button pressed, get password from input box, encrypt it, and display it in the GUI
def encrypt(password_input):
    # get password from input box
    password = password_input.get()
    
    # check if password is empty
    if password == "":
        # show error message
        tk.messagebox.showerror("Error", "Please enter a password!")
        # get password from input box
        password_input.delete(0, tk.END)
        # get password from input box
        password = password_input.get()
        
    # if password is not empty, encrypt it and display it in the gui
    else:
        # encrypt password using main module
        encrypted_password = main.small_password_encrypt(password)
        # create label with text from main.py
        password_display = tk.Label(text=encrypted_password, bg='#2D2B55', fg="#FF7200", font='Helvetica 8 bold')
        # pack label into window
        password_display.pack()
        # delete password from input box
        password_input.delete(0, tk.END)