from django.urls import path
from .views import *

urlpatterns = [
    path('/home', BookListView.as_view(), name="book_init"),
]
