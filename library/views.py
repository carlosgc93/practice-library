from django.shortcuts import render


# Create your views here.
def index_library(request):
    return render(request, "index-library.html")
