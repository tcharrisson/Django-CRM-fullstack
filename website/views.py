from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customer

@login_required
def home(request):
    query = request.GET.get('q', '')
    customers = Customer.objects.filter(user=request.user)
    if query:
        customers = customers.filter(name__icontains=query)
    return render(request, 'home.html', {'customers': customers, 'query': query})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        messages.error(request, 'Form errors')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_customer(request):
    return render(request, 'add_customer.html')  # Placeholder

@login_required
def update_customer(request, pk):
    return render(request, 'update_customer.html')  # Placeholder

@login_required
def delete_customer(request, pk):
    return render(request, 'delete_customer.html')  # Placeholder