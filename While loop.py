import mysql.connector 
result = mysql.connector.connect(user = "root", password = "rootpassword", host = "localhost")
print(result)