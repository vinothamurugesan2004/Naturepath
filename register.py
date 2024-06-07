#!c:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

Form=cgi.FieldStorage()

FFullName=Form.getvalue('name')
FEmail=Form.getvalue('email')
FMessage=Form.getvalue('message')

print("<h1>",FFullName, FEmail, FMessage,"<h1>")
print("<h3> Thank You For Your Enquiry </h3>")

mydb=mysql.connector.connect(
    host="Localhost",
    user="root",
    password="",
    database="naturepath adventures"
)

mycursor=mydb.cursor();

sql="INSERT INTO enquiry(FullName,Email,Message) VALUES(%s, %s, %s)";
val=(FFullName, FEmail, FMessage)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")