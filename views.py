from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def property_list(request):
    properties = Property.objects.filter(is_published=True).order_by('-list_date')
    return render(request, 'housing/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'housing/property_detail.html', {'property': property})

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.owner = request.user
            prop.save()
            messages.success(request, 'Property added successfully!')
            return redirect('housing:property_detail', pk=prop.pk)
    else:
        form = PropertyForm()
    return render(request, 'housing/property_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your account is created.")
            return redirect('housing:property_list')
    else:
        form = UserRegisterForm()
    return render(request, 'housing/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('housing:property_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'housing/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('housing:login')
def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'housing/about.html') 

def properties(request):
    return render(request, 'properties.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')