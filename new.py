# print('hello')
# input("Enter your ID: ")

a = [1,2,3,4,'Hello',[1,2,3]]
b = {1,1,1,2,3,3,2,2,1}
my_dict = {'Name':'Joe','Age':'10','Countries':['Israel','Spain','England']}

# if 5 > 2:
#     print("Yes")
# elif 10 > 5:
#     print("Yes2")
# else:
#     print("No")

###################################################
#LOOPS
#FOR - רץ על כמות איברים סופית - ידועה מראש
my_dict = {'Name':'Joe','Age':'10','Countries':['Israel','Spain','England']}

# for x in my_dict: #ריצה על המפתחות - על צד שמאל
#     print(x)

# for x in my_dict.values(): #ריצה על הערכים - צד ימין
#     print(x)

# for x in my_dict.items(): #ריצה על מפתחות וערכים ביחד 
#     print(x)

# for key,value in my_dict.items(): #ריצה על שניהם אבל מופרדים - לא ביחד
#     print(key,value)


#WHILE - לולאה שיש לה התנייה - כמות הריצות לא ידועה מראש ברוב המקרים

# age = int(input("Enter your age: "))
# attempts = 1

# while age < 18:
#     if attempts == 3:
#         print("You are blocked!")
#         break
#     else:
#         print("Not Allowed!")
#         age = int(input("Try again, Enter your age: "))
#         attempts += 1


############################################################################
# try:
#     # num1 = int(input("Enter your first number: "))
#     # num2 = int(input("enter num2: "))
#     # print(num1 / num2)
#     my_list = [1,2,3]
#     print(my_list[30])

# except ZeroDivisionError:
#     print('Make sure you entered valid numbers for division')
# except IndexError:
#     print("Invalid index!") 
# except:
#     print("Error!")

########################################################
#FUNCTIONS
def example1():
    print("Hello")

def example2(num1,num2):
    print(num1+num2)

def example3(num1=10,num2=50): #ברירת מחדל - רק אם לא הכנסתי מספרים בעצמי הוא ישתמש בהם
    print(num1+num2)



#RETURN - להחזיר את הערך החוצה - שיהיה אפשר לשמור אותו
#RETURN - מסיים את הפונקציה, כל מה שיבוא אחרי לא ירוץ
def example4():
    return 10+20
    print("Hello")


##################################################
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    else:
        return "Invalid username or password"


def main():
    example1()
    example2(10,30)
    login('Test','1234')
    
if __name__ == '__main__':
    main()


###########################################################
#API  - פרוטוקול של תקשורת ותעבורת מידע בין אפליקציות \ אתרים \ מחשבים

#GET - בקשה לקבלת מידע
#POST - בקשה לשליחת מידע
#DELETE - בקשה למחיקת מידע
#UPDATE \ PUT \ PATCH - בקשה לעדכון מידע קיים
#JSON - מילון - DICTIONARY
#RESPONSE - תשובה שקיבלתי על הבקשה ששלחתי - לא משנה איזה סוג בקשה
#STATUS CODE - קוד מספרי שמהווה סטטוס של הבקשה ששלחתי - האם תקין \ לא תקין
#200-299 - קוד של בקשה תקינה
#300-399 - REDIRECT \ חצי שגיאה \ עדכון מידע
#400-499 - שגיאות
#500-599 - עוד סוג של שגיאות

import requests

def send_get_request(url):
    response = requests.get(url)
    print(response.status_code)
    try:
        json_data = response.json()
        print(json_data)
        return json_data
    except ValueError:
        print("Response is not in JSON format")
        return response.text



data = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())


##########################################################################
#SQL - Structured Query Language
#שפה לשליפת מידע בפורמט טבלאי
#SELECT name,email FROM users


#SQLITE - סוג של מסד נתונים
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()



#FLASK - יצירת אתרים \ דפי אינטרנט דרך פייתון
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return f"Hello"

@app.route('/users')
def users():
    return f"Hello this is users"

if __name__ == '__main__':
    app.run(debug=True)
