from django.shortcuts import render,redirect
from .models import Expense
from django.contrib import messages
from django.db.models import Q
from django.db import connection
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully. please log in.")
            return redirect('login')
        else:
            messages.error(request,"Please correct the errors below")

    else:
        form=RegisterForm()

    return render(request,'register.html',{"form":form})


def index(request):
    expense=Expense.objects.all()
    query=""
    if request.method=="POST":
       if "add" in request.POST:
           title=request.POST.get("title")
           category=request.POST.get("category")
           amount=request.POST.get("amount")
           Expense.objects.create(title=title,category=category,amount=amount)
           messages.success(request,"Expense Added Successfully")

       elif "update" in request.POST:
           id=request.POST.get("id")
           title=request.POST.get("title")
           category=request.POST.get("category")
           amount=request.POST.get("amount")
           update_expense=Expense.objects.get(id=id)
           update_expense.title=title
           update_expense.category=category
           update_expense.amount=amount
           update_expense.save()
           messages.success(request,"Expense Updated Successfully")
           
       elif "delete" in request.POST:
           id=request.POST.get("id")
           Expense.objects.get(id=id).delete()
           messages.success(request,"Expense Deleted Successfully")
           reset_expense_sequence()         # id reset
           return redirect('index')  

       elif "search" in request.POST:
           query=request.POST.get("searchquery")
           expense=Expense.objects.filter(Q(title__icontains=query) | Q(amount__icontains=query) | Q(category__icontains=query))

    context={"expense":expense,"query":query}
    return render(request,"index.html",context=context)

def reset_expense_sequence():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses_expense'")


def cust_logout(request):
    print("in logout")
    return render(request,"logout.html")
