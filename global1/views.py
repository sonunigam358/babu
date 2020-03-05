from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def global1(request):
	return HttpResponse("<h1 style='color:red;text-align:center'>HELLO DJANGO</h1>")
def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')
def services(request):
	return render(request,'services.html')
def help(request):
	return render(request,'help.html')
def form(request):
	return render(request,'form.html')