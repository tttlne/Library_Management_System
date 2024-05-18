from tkinter import *
from tkinter import messagebox
from main import main_menu  # Import hàm main_menu từ tệp main.py
from connect_database import connect_to_database

# Hàm kiểm tra đăng nhập
def check_login(username, password, root):
    con, cur = connect_to_database()  # Sử dụng hàm connect_to_database từ connect_database.py
    
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cur.execute(query, (username, password))
    result = cur.fetchone()
    
    if result:
        messagebox.showinfo("Login Success", "Welcome to the Library System")
        root.destroy()
        main_menu()  # Gọi hàm main_menu đã được import từ main.py
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Hàm thoát chương trình
def on_closing(root):
    root.destroy()
    exit()

# Hàm đăng nhập
def login():
    global username_entry, password_entry, root
    
    root = Tk()
    root.title("Login")
    root.geometry("400x300")

    # Gắn sự kiện đóng cửa sổ với hàm on_closing
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    
    Label(root, text="Username").pack(pady=10)
    username_entry = Entry(root)
    username_entry.pack(pady=10)
    
    Label(root, text="Password").pack(pady=10)
    password_entry = Entry(root, show="*")
    password_entry.pack(pady=10)
    
    Button(root, text="Login", command=lambda: check_login(username_entry.get(), password_entry.get(), root)).pack(pady=20)
    
    root.mainloop()

