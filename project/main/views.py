import pprint
from django.shortcuts import render , redirect
from main.services import Netatmo_Client
from django.http import HttpRequest, HttpResponse
from .utils.utils import check_user
from .models import DeviceModel, Patient

# Create your views here.
# 
netatmo_client = Netatmo_Client()
# Create your views here. 
def index(request):
    return render(request, 'login.html',)

def autorize(request: HttpRequest):
    state = request.GET.get('state')
    code = request.GET.get('code')

    if state is None or code is None:
        return HttpResponse("Error")
    
    netatmo_client.access_token(code)
    data = netatmo_client.get_data(netatmo_client.access_token_)

    #create a session with the tokens
    request.session['access_token'] = netatmo_client.access_token_
    request.session['refresh_token'] = netatmo_client.refresh_token

    print(request.session['access_token'])

    
    # netatmo_client.refresh_token

    request.session['email'] = data['body']['user']['mail']
    check_user(request.session['email'])

    print(request.session.__dict__)
    # pprint.pprint(data)

    return redirect('devices')

def login_netatmo(request):
    return redirect(netatmo_client.login())



def devices(request):
    # print(request.session['access_token'])
    # print(request.session['refresh_token'])
    # print(request.session['email'])

    devices = netatmo_client.deserialize_devices(netatmo_client.get_data(request.session['access_token'])['body']['devices'])
    # print('\n\n\n')
    # print('==============DEVICES:-------------------')
    # print(devices)
    # print('\n\n\n')

    return render(request, 'devices.html', {'devices':devices})


def logout(request):
    request.session.flush()
    return redirect('index')


def create_patient(request):
    created_patient = Patient.objects.create(
        rut = request.POST['inputRut'],
        nombre = request.POST['inputNombre'],
        edad = request.POST['inputEdad'],
        numero_contacto = request.POST['inputNContacto'],
        nombre_contacto = request.POST['inputNombreContacto'],
        condicion = request.POST['inputCondicion']
    )
 
    print(request.POST)
    return redirect('devices')



def read_patient(request):
    patients = Patient.objects.all()
    print(patients)
    return render(request, 'patients.html', {'patients': patients})

def update_patient(request, id):
    patientFound = Patient.objects.get(id=id)
    formulario = Patient(request.POST or None, instance=patientFound)
    if formulario.is_valid() and request.method == 'POST':
        formulario.update()
        return redirect('devices')
    return render(request,'devices')

def delete_patient(request, id):
    patientDelete = Patient.objects.get(id = id)
    patientDelete.delete()
    return redirect('devices.html')

#def devices_paciente(request):
#    
#    return render(device_paciente)
#
#