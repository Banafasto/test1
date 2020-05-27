import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='mapuser', password='mapuser',
                                  host='192.168.1.9', database='map')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("You are connected!")

    curA = cnx.cursor(buffered=True)

    query = ("SELECT * FROM MyGuests;")

    curA.execute(query)
    result = curA.fetchall()
    print(result[0])
    cnx.close()
