from django.http import HttpResponse
from django.shortcuts import render
def dashboard_page(request):
    return render(request,"dashboard.html")
def contact(request):
    return render(request,"contact.html")
def html(request):
    return render(request,"hi.html",{"name":"Sazzad","address":"basay"})
