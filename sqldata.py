import mysql.connector  

connection = mysql.connector.connect(host='127.0.0.1',user='root',password="mohan" ,database='axixa')
    

cursor = connection.cursor()

name = input("enter name: ")
email = input("Enter email: ")
mobile = input("Enter Mobile number : ")

if name.strip() == "" or email.strip() == "" or mobile.strip() == "":
    print("Name, Email, and Mobile number cannot be empty.")
    
elif email.endswith("@gmail.com"):
    print("Email must end with '@gmail.com'.")
elif len(mobile) != 10:
    print("Mobile number must be exactly 10 digits.")
    
else:
    query = "INSERT INTO stu (name, email, mobile) VALUES (%s, %s, %s)"
    values = (name, email, mobile)
    cursor.execute(query, values)
    connection.commit()
    print("Invalid email! Please enter a Gmail address (must end with @gmail.com)."))
