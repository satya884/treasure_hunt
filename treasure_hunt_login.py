import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess 

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='haha')
# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Create labels and entry widgets for email and password
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


def dashboard():
    cursor=conn.cursor()
    email = email_entry.get()
    pas = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, pas))
    p=cursor.fetchall()
    win = tk.Tk()
    win.Title=("Dashboard")
    user = tk.Label(win, text=p[0])
    user.pack()
    conn.commit()
    conn.close()
    
def save_to_database():
    cursor = conn.cursor()
    
    email = email_entry.get()
    password = password_entry.get()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (email VARCHAR(255), password VARCHAR(255))')
    cursor.execute('INSERT INTO users VALUES (%s, %s)', (email, password))

    conn.commit()
    conn.close()

    messagebox.showinfo('Success', 'User registered successfully!')
    
# Function to check if the email and password are valid    
def login():
    email = email_entry.get()
    pas = password_entry.get()

    # Here, you can add your own validation logic to check if the email and password are valid.
    # For example, you can check if the email and password match a record in a database.
    # If the email and password are valid, show a success message.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, pas))
    p=cursor.fetchall()
    
    if email == p[0][0] and pas == p[0][1]:
        print("Login Successful")
        root.destroy()
        subprocess.call(["python","C:\\Users\\satya\\OneDrive\\Documents\\treasure_hunt.py"])
    else:
        failure_label = tk.Label(root, text="Login failed!", fg="green")
        failure_label.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

register_button = tk.Button(root, text="Register", command=save_to_database)
register_button.pack()

dash_button = tk.Button(root, text="dashboard", command=dashboard)
dash_button.pack()
root.mainloop()


    

