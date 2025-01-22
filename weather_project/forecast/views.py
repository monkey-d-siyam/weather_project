from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import FavoriteCityForm
from .models import UserProfile, City
from .utils import get_weather_data  # Import the function

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
                UserProfile.objects.get_or_create(user=user)  # Ensure user profile creation
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
    weather_condition = None
    if 'city' in request.GET:
        city = request.GET['city']
        weather_data = get_weather_data(city)
        if weather_data:
            weather_condition = weather_data['description']
    return render(request, 'forecast/index.html', {'weather_data': weather_data, 'weather_condition': weather_condition})


@login_required
def profile(request):
    user = request.user
    password_form = PasswordChangeForm(request.user)
    favorite_city_form = FavoriteCityForm()

    if request.method == 'POST':
        if 'username' in request.POST:
            user.username = request.POST['username']
            user.save()
            password_form = PasswordChangeForm(request.user)
        elif 'old_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keep the user logged in after password change
        elif 'name' in request.POST and 'country' in request.POST:
            favorite_city_form = FavoriteCityForm(request.POST)
            if favorite_city_form.is_valid():
                city = favorite_city_form.save()
                user.userprofile.favorite_cities.add(city)
                user.userprofile.save()
                return redirect('profile')

    favorite_cities = user.userprofile.favorite_cities.all()

    return render(request, 'forecast/profile.html', {
        'user': user,
        'password_form': password_form,
        'favorite_city_form': favorite_city_form,
        'favorite_cities': favorite_cities
    })