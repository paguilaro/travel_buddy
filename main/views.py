from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import User, Travels


@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


@login_required
def travels(request):

    travels= Travels.objects.all().order_by('-created_at')[:5]
    context = {
        'saludo': 'Hola',
        "travels":travels
    }
    return render(request, 'travels.html', context)

@login_required
def addtrip(request):
    if request.method=='GET':
        return render(request, 'addtrip.html')
    else:   
        destination= request.POST['destination']
        description= request.POST['description']
        travel_from= request.POST['travel_from']
        travel_to= request.POST['travel_to']
        # traer el id del usuario
    #try:   
        #user=User.objects.create(name=request.POST['user_id'])
        # crear el nuevo Travel
        #travel=Travels.objects.create(destination=destination, description=description, travel_from=travel_from, travel_to=travel_to)
        # redirigir al Home
        #return redirect(/addtrip)

#   travel=request.POST['travels']
#   if request.POST['new_travel'] !='':
#   travel=Travels.objects.create(name=request.POST['destination'])

@login_required
def view(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'view.html', context)