from random import choice
from string import ascii_lowercase, ascii_uppercase
import json
from ..models import User

#here needs to be a function that will return a random string

def get_random_string():
    """"returns a random string of 15 characters"""
    numbers = "1234567890"
    characters = numbers + ascii_uppercase + ascii_lowercase
    return ''.join(choice(characters) for _ in range(15))


#this class convert the device json into a object
class Device(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

#this class convert the DashbordData json into a object
class DashboardData(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


#this function check if the user exists in the database by email and if not it will create a new user
def check_user(email):
    user = User.objects.filter(email=email).first()
    print(email)
    print(user)
    if not user:
        user = User.objects.create(email=email)
    return user
