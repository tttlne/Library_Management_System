from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own database name and password here to reflect in the code

# to run it on MYSQL server on CMD code: mysql -u root -p
# 
# create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
# create table books_issued(bid varchar(20) primary key, issuedto varchar(30));


root = Tk()
root.title("Library")
root.geometry("725x375")

# Load the background image
background_image = Image.open("image/Library.jpg")  # Update this path
bg_img = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image
background_label = Label(root, image=bg_img)
background_label.place(relwidth=1, relheight=1)

# Create a Frame for the heading
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to VNU_Lic Library", bg='#8B4513', fg='white', font=('Times New Roman', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Define the color for the buttons
button_bg_color = "#8B4513"  # Dark brown color
button_fg_color = "white"

# Add buttons on top of the background image
btn1 = Button(root, text="Add Book Details", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 13), command=addBook)
btn1.place(relx=0.33, rely=0.38, relwidth=0.35, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 13), command=delete)
btn2.place(relx=0.33, rely=0.49, relwidth=0.35, relheight=0.1)

btn3 = Button(root, text="View Book List", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 13), command=View)
btn3.place(relx=0.33, rely=0.6, relwidth=0.35, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 13), command=issueBook)
btn4.place(relx=0.33, rely=0.71, relwidth=0.35, relheight=0.1)

btn5 = Button(root, text="Return Book", bg=button_bg_color, fg=button_fg_color, font=('Times New Roman', 13), command=returnBook)
btn5.place(relx=0.33, rely=0.82, relwidth=0.35, relheight=0.1)

root.mainloop()
