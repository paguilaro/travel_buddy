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

    travels= Travels.objects.all()[:5]
    context = {
        'saludo': 'Hola',
        "travels":travels
    }
    return render(request, 'travels.html', context)

@login_required
def addtrip(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'addtrip.html', context)