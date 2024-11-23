from django.urls import path
from .views import get_books,add_books,book_detail

urlpatterns = [
    path('books/',get_books,name='get_books'),
    path('books/add/',add_books,name='add_books'),
    path('books/<int:pk>/',book_detail,name='book_detail'),
]