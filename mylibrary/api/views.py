from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from .serializer import BooksSerializer

# Create your views here.

@api_view(['GET'])
def get_books(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_books(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def book_detail(request,pk):
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)