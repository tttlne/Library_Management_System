from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# kết nối với cơ sở dữ liệu
mypass=""
mydatabase=""

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Table Names
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    # tạo giao diện delete book
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, con, cur, bookTable, root
