from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_client = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True)
    id = models.IntegerField(unique=True)
    client_name = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=264)


class Project(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True)
    id = models.IntegerField(unique=True)
    project_name = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=264)
