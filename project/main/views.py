from django.shortcuts import render
from .credentials import credentials
# Create your views here.
def index(request):
    print(credentials.client_id)
    print(credentials.client_secret)
    return render(request, 'index.html',)

