from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def auth(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login Successful')
        else:
            return HttpResponse('Login Failed')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('User already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request, 'cadastro.html', {'success': 'User created successfully'})


# def plataforma(request):
#     if request.user.is_authenticated:
#         return HttpResponse('Plataforma')
#     else:
#         return HttpResponse('Você deve fazer login para acessar essa página')

# @login_required
@login_required(login_url='/usuarios/login/')
def plataforma(request):
    return render(request, 'plataforma.html')


def sign_out(request):
    logout(request)
    return redirect('usuarios:login')
