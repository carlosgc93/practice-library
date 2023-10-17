from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hola(request):
    return render(request,"index-book.html")