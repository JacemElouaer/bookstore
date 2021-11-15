from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from  django.contrib.auth.forms import UserCreationForm
from  .forms import CreateNewUser
from  django.contrib import messages

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    n_orders = orders.count()
    p_orders = orders.filter(status="Pending").count()
    d_orders = orders.filter(status="Delivered").count()
    out_orders = orders.filter(status="Out of order").count()
    in_orders = orders.filter(status="In progress").count()
    data = {'customers': customers,
            'orders': orders,
            'n_orders': n_orders,
            'p_orders': p_orders,
            'd_orders': d_orders,
            'out_orders': out_orders,
            'in_orders': in_orders}
    return render(request, 'bookstore/dashboard.html', data)


def books(request):
    book = Book.objects.all()
    return render(request, 'bookstore/books.html', {'books': book})


def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    myFilter = OrderFilter(request.GET , queryset=orders)
    orders =  myFilter.qs
    context = {'customers': customers, "myFilter": myFilter,'orders': orders}
    return render(request, 'bookstore/customer.html', context)


# def create(request):
#     form = OrderForm()
#     context={'form' :form}
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request,  'bookstore/my_order_form.html' ,context)

def create(request, pk):
    orderFormset = inlineformset_factory(Customer, Order, fields=('book', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = orderFormset(instance=customer)
    form = OrderForm()
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'bookstore/my_order_form.html', context)


def update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'bookstore/my_order_form.html', context)


def delete(request, pk):
    order = Order.objects.get(id=pk)
    context = {"order": order}
    if request.method == "POST":
        order.delete()
        return redirect("/")
    return render(request, 'bookstore/delete_form.html', context)

# def name_creater_method (resquest , otherparams):
#     form =  instance_class_formcreator()
#     context ={set_the_context_with_data}
#     if form.method =="POST" :
#         form =  create_new_form(request.POST)

# Create your views here.


def login(request):
    form  =  UserCreationForm()
    context={'form':form}
    return render(request, 'bookstore/login.html', context)

def register(request):

    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            user =  form.cleaned_data.get('username')
            messages.success(request ,  user + ' has been created ! ')
            return redirect('login')
    context ={"form":  form}
    return render(request, 'bookstore/register.html', context)
