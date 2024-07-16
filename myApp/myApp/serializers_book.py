from rest_framework import serializers
from .models import Book

 #BookSerializer inherites from ModelSerializer
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model= Book
        fields = ['id','Author','title','description']