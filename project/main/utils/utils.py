from random import choice
from string import ascii_lowercase, ascii_uppercase
import json
from main.models import User
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
        return f"{diff.days} dias"
    elif diff.seconds > 3600:
        return f"{diff.seconds // 3600} horas"
    else:
        return f"{diff.seconds // 60} minutos"


#Air Quality Health Index
#This function returns the Air Quality Health Index and the color of the index
def health_index_state_color(health_index):

    if health_index == 0:
        return "Saludable", "132,224,255" #lightblue
    elif health_index == 1:
        return "Bueno", "180,241,208" #green
    elif health_index == 2:
        return "Aceptable", "247,247,171" #yellow
    elif health_index == 3:
        return "Regular", "255,165,82" #orange
    elif health_index == 4:
        return "Insalubre", "226,101,101" #red


#this functions returns the wifi status of the device in a string
def wifi_status(wifi):
    if wifi <= 65:
        return "Buena conexión", 4, 'green'

    elif wifi >= 66 and wifi <=80:
        return  "Media conexión", 2, 'yellow'

    elif wifi >= 81:
        return  "Mala conexión", 1, 'red'

    
#this functions remove the ':' from the mac
def id_format(id_):
    return f"K{id_.replace(':', '')}"



# def relate(dashboard_data):

    

#     if dashboard_data.Humidity:



def mensajes(dashboard_data):

    relatos = []

    mensaje_humedad=""
    humedad=dashboard_data.Humidity
    if humedad > 70:
        mensaje_humedad="Demaciado Humedo"
        if humedad > 50:
            mensaje_humedad="Zona de confort"
            if humedad > 30:
                mensaje_humedad="Normal"
    mensaje_ruido=""
    ruido=dashboard_data.Noise
    if ruido > 140:
        mensaje_ruido="Ruido excesivo"
        if ruido > 90:
            mensaje_ruido="Mucho ruido"
            if ruido > 50:
                mensaje_ruido="Ruido de gente"
                if ruido > 20:
                  mensaje_ruido="Agradable"
    mensaje_co2=""
    co2=dashboard_data.CO2
    if co2 > 2100:
        mensaje_co2="Ambiente altamente contaminado"
        if co2 > 1500:
            mensaje_co2="Ambiente contaminado"
            if co2 > 1000:
                mensaje_co2="Ambiente Normal"
                if co2 > 800:
                   mensaje_co2="Ambiente Bueno"
                   if co2 > 600:
                      mensaje_co2="Ambiente Excelente"

    mensaje_temperatura=""
    temperatura=dashboard_data.Temperature
    if temperatura > 50:
        mensaje_humedad="Calor Excesivo"
        if temperatura > 35:
            mensaje_temperatura="Demaciado calor"
            if temperatura > 20:
                mensaje_temperatura="Normal"
                if temperatura > 10:
                   mensaje_temperatura="Demaciado frio"

    return ({'mensaje_humedad': mensaje_humedad, 'mensaje_ruido':mensaje_ruido, 'mensaje_co2':mensaje_co2,'mensaje_temperatura':mensaje_temperatura})

