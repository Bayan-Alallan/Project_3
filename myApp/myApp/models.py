from django.db import models

class Book(models.Model):
    Author=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    
    def __str__(self):
        return  self.Author   +  "  "  +  self.title 