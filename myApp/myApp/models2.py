from django.db import models
from django.contrib.auth.models import User

class User_Info(models.Model):
      username=models.CharField(max_length=200)
      first_name=models.CharField(max_length=200)
      last_name=models.CharField(max_length=200)
      email=models.CharField(max_length=200)

      def __str__(self):
        return self.username
