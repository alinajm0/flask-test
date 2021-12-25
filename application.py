import mysql.connector
import webbrowser
from flask import Flask

app = Flask(__name__)

conn = mysql.connector.connect(user='root', password='',
                              host='localhost',database='test')
print(conn)

if conn:
    print ("Connected Successfully")

else:
    print ("Connection Not Established")




select_employee = """SELECT * FROM users"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()
print(cursor)
print(result)

# p = []

# tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
# p.append(tbl)

# for row in result:
#     a = "<tr><td>%s</td>"%row[0]
#     p.append(a)
#     b = "<td>%s</td>"%row[1]
#     p.append(b)
#     c = "<td>%s</td>"%row[2]
#     p.append(c)
#     d = "<td>%s</td></tr>"%row[3]
#     p.append(d)


# contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
# <html>
# <head>
# <meta content="text/html; charset=ISO-8859-1"
# http-equiv="content-type">
# <title>Python Webbrowser</title>
# </head>
# <body>
# <table>
# %s
# </table>
# </body>
# </html>
# '''%(p)

# filename = 'webbrowser.html'

# def main(contents, filename):
#     output = open(filename,"w")
#     output.write(contents)
#     output.close()

# main(contents, filename)    
# webbrowser.open(filename)

# if(conn.is_connected()):
#     cursor.close()
#     conn.close()
#     print("MySQL connection is closed.")




# from cs50 import SQL
# from flask import Flask, render_template, request

# app = Flask(__name__)

# db = SQL("sqlite:///data.db")


# @app.route("/")
# def index():
#     data = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%")
#     return render_template("search.html", shows=shows)