import pymysql

def connect_to_database():
    mypass = "nam2012004"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    return con, con.cursor()
