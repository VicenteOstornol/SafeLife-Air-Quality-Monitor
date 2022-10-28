from django.shortcuts import render , redirect
from main.services import Netatmo_Client
from django.http import HttpRequest, HttpResponse
from .utils.utils import check_user
from .models import DeviceModel, Patient


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

    return redirect('devices')

def login_netatmo(request):
    return redirect(netatmo_client.login())



def devices(request):

    devices = netatmo_client.deserialize_devices(netatmo_client.get_data(request.session['access_token'])['body']['devices'])

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
        condicion = request.POST['inputCondicion'],
        device = DeviceModel.objects.get(mac_ad=request.POST['inputAmbiente'])
    )
    print(request.POST['inputAmbiente'])

    return redirect('devices')


def read_patient(request):
    patients = Patient.objects.all()
    devices = netatmo_client.deserialize_devices(netatmo_client.get_data(request.session['access_token'])['body']['devices'])
    print(patients)
    return render(request, 'patients.html', {'patients': patients,'devices':devices})


def update_patient(request, pk):
    patientUpdate = Patient.objects.filter(id=pk).update(
        rut=request.POST['inputRut'],
        nombre=request.POST['inputNombre'],
        edad=request.POST['inputEdad'],
        numero_contacto=request.POST['inputNContacto'],
        nombre_contacto=request.POST['inputNombreContacto'],
        condicion=request.POST['inputCondicion'],
        device=DeviceModel.objects.get(mac_ad=request.POST['inputAmbiente'])
    )
    
    
    return redirect('patients')
    

def delete_patient(request,pk):
    patientDelete = Patient.objects.get(id=pk)

    try:
        patientDelete.delete()
    except:
        pass


    return redirect('patients')