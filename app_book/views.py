from django.shortcuts import render
from .models import *
from django.views.generic import ListView


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "index-book.html"