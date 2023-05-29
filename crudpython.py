import mysql.connector

koneksi = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "crud_py",
)

mycursor = koneksi.cursor()

next = True
while next:
    print("")
    print("")
    print("")
    print("DATA USER")
    print("1. Read")
    print("2. Create")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit")
    print("")

    p = int(input("Select Menu"))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("====================")
        print("(id,name,email,phone)")
        for x in myresult:
            print(x)
    elif(p == 2):
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        sql = "INSERT INTO user (name, email, phone) VALUES (%s, %s, %s)"
        val = (name, email, phone)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "add data successfully")
    elif(p == 3):
        id = input("ID USER: ")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x 
        if(user != None):
            name = input("NAME("+user[1]+") :") or user[1]
            email = input("EMAIL("+user[2]+") :") or user[2]
            phone = input("PHONE("+user[3]+") :") or user[3]
            sql = "UPDATE user SET name=%s,email=%s,phone=%s WHERE id=%s"
            val = (name, email, phone, id)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user saved")
        else:
                print("data not found")
    elif(p == 4):
        id = input("ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("DATA DELETED :", user)
            sql = "DELETE FROM user WHERE id="+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data user deleted!")
        else:
            print("data not found")
    elif(p == 5):
        next = False
            

