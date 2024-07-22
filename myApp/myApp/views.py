from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .models2 import User_Info
from .serializers_book import BookSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



@api_view(['POST', 'GET','PUT', 'DELETE'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            })
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
         
        @authentication_classes([TokenAuthentication])
        @permission_classes([IsAuthenticated])
        def get_users(request):

            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
     
    elif request.method == 'PUT':
        
        # Safely get the 'id' from the request data
         user_id = request.data.get('id')
         if user_id is None:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
         try:
            # Attempt to get the User instance
            user = User.objects.get(id=user_id)
         except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
         serializer = UserSerializer(user, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        # Safely get the 'id' from the request data
        user_id = request.data.get('id')
        if user_id is None:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Attempt to get the User instance
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








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
    



