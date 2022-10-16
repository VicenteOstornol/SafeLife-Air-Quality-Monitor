from random import choice
from string import ascii_lowercase, ascii_uppercase
import json
from ..models import User
from datetime import datetime
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


#this function calcule with timestamp the update ago time
def update_ago(timestamp):
    now = datetime.now()
    update = datetime.fromtimestamp(timestamp)
    diff = now - update
    if diff.days > 0:
        return f"{diff.days} days ago"
    elif diff.seconds > 3600:
        return f"{diff.seconds // 3600} hours ago"
    else:
        return f"{diff.seconds // 60} minutes ago"


#Air Quality Health Index
#This function returns the Air Quality Health Index and the color of the index
def health_index_state_color(health_index):

    if health_index == 0:
        return "Healthy", "lightblue"
    elif health_index == 1:
        return "Fine", "green"
    elif health_index == 2:
        return "Fair", "yellow"
    elif health_index == 3:
        return "Poor", "orange"
    elif health_index == 4:
        return "Unhealthy", "red"

