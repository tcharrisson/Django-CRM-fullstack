from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm

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
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, 'Customer added successfully.')
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'website/add_customer.html', {'form': form})


@login_required
def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully.')
            return redirect('home')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'website/update_customer.html', {'form': form})


@login_required
def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully.')
        return redirect('home')
    return render(request, 'website/delete_customer.html', {'customer': customer})