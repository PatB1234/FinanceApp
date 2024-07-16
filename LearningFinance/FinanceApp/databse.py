import sqlite3 as driver
from sqlite3.dbapi2 import Cursor
from pydantic import BaseModel
from FinanceApp.models import User

# DB_URL
DATABASE_URL = '../db.sqlite3'

# class User(BaseModel):

#     username: str
#     email: str
#     password: str
#     uid: int


def cursor_func(function, fetch):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    try:

        cursor.execute(function)
        if (fetch):
            records = cursor.fetchall()
            return records

        database.commit()
    except:

        database.rollback()


def getUsers():

    arr = []
    for user in User.objects.all():

        arr.append(User(id=user.id, name=user.name,
                        email=user.email, password=user.password))
    return arr


def getUserIDByEmail(email: str):

    for user in User.objects.all():

        if user.email == email:

            return user.id
# Login & Sign-Up Functions


def loginCheck(email: str, password: str):

    users = getUsers()
    for user in users:

        if user.email == email and user.password == password:

            return True

    return False


def createUser(name: str, email: str, password: str):

    try:

        newUser = User(name=name, email=email, password=password)
        newUser.save()
        print("Successful")
    except:

        raise Exception("An error has occured:")
