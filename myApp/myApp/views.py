from rest_framework.decorators  import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

from django.contrib.auth import authenticate, login, logout
from .loginForm import login_view, logout_view

# Add the rest of your views here

from django.shortcuts import render, redirect 
from .loginForm import LoginForm



@api_view(['GET', 'POST'])
def book_list(request,format=None):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer (book, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])

def book_detail(request,id):

    try:
        book=Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method =='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data)

    
    elif request.methos=="PUT":
        serializer=BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



