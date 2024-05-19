from tkinter import *
from tkinter import messagebox
from connect_database import connect_to_database
from main import main_menu

# Hàm kiểm tra đăng nhập
def check_login(username, password, root):
    con, cur = connect_to_database()
    
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cur.execute(query, (username, password))
    result = cur.fetchone()
    
    if result:
        messagebox.showinfo("Login Success", "Welcome to the Library System")
        root.destroy()
        main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

    cur.close()
    con.close()

# Hàm tạo tài khoản
def create_account():
    def save_account(username, password, confirm_password, root):
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        con, cur = connect_to_database()
        
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cur.execute(query, (username, password))
        con.commit()
        
        messagebox.showinfo("Account Created", "Account created successfully. You can now log in.")
        cur.close()
        con.close()
        
        root.destroy()
        login()
    
    root = Tk()
    root.title("Create Account")
    root.geometry("400x400")

    frame = Frame(root, bg='#ffffff', padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Create a new account", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
    
    Label(frame, text="Username", bg="#ffffff").pack(pady=5)
    username_entry = Entry(frame, font=("Helvetica", 12))
    username_entry.pack(pady=5)
    
    Label(frame, text="Password", bg="#ffffff").pack(pady=5)
    password_entry = Entry(frame, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=5)
    
    Label(frame, text="Confirm Password", bg="#ffffff").pack(pady=5)
    confirm_password_entry = Entry(frame, show="*", font=("Helvetica", 12))
    confirm_password_entry.pack(pady=5)

    show_password_var = BooleanVar()
    Checkbutton(frame, text="Show Password", variable=show_password_var, command=lambda: toggle_password_visibility(password_entry, confirm_password_entry, show_password_var), bg="#ffffff").pack(pady=5)
    
    Button(frame, text="Create Account", command=lambda: save_account(username_entry.get(), password_entry.get(), confirm_password_entry.get(), root), font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=20)
    
    root.mainloop()

def toggle_password_visibility(password_entry, confirm_password_entry, show_password_var):
    if show_password_var.get():
        password_entry.config(show="")
        confirm_password_entry.config(show="")
    else:
        password_entry.config(show="*")
        confirm_password_entry.config(show="*")

# Hàm thoát chương trình
def on_closing(root):
    root.destroy()
    exit()

def toggle_password_visibility_login(password_entry, show_password_var):
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Hàm đăng nhập
def login():
    global username_entry, password_entry, root
    
    root = Tk()
    root.title("Login")
    root.geometry("400x450")

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    
    frame = Frame(root, bg='#ffffff', padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Login", bg="#ffffff", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    Label(frame, text="Username", bg="#ffffff", font=("Helvetica", 12)).pack(pady=10)
    username_entry = Entry(frame, font=("Helvetica", 12))
    username_entry.pack(pady=10)
    
    Label(frame, text="Password", bg="#ffffff", font=("Helvetica", 12)).pack(pady=10)
    password_entry = Entry(frame, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=10)
    
    show_password_var = BooleanVar()
    Checkbutton(frame, text="Show Password", variable=show_password_var, command=lambda: toggle_password_visibility_login(password_entry, show_password_var), bg="#ffffff").pack(pady=5)

    Button(frame, text="Login", command=lambda: check_login(username_entry.get(), password_entry.get(), root), font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=20)
    
    root.mainloop()

def start_program():
    con, cur = connect_to_database()
    
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    
    cur.close()
    con.close()
    
    if count == 0:
        create_account()
    else:
        login()

