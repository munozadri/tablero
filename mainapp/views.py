from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def tablero(request):
    return render(request,'mainapp/tablero.html',
    {'title': 'Tableros'
    })

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tableros')
        
        else:
            messages.warning(request, 'No te has identificado correctamente')

        
    return render(request,'users/login.html',{
        'title':'Login'
        })


def logout_user(request):
    logout(request)

    return redirect('login')

