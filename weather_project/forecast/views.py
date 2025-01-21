from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .utils import get_weather_data

def home(request):
    return render(request, 'forecast/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'forecast/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'forecast/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def index(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        weather_data = get_weather_data(city)
    return render(request, 'forecast/index.html', {'weather_data': weather_data})