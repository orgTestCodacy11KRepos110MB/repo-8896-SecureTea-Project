from django.db import models

# Create your models here.

class User(models.Model):
    """
    This is a class for building user model

    Attributes:
        id (int): Id of the user (autoincremental)
        username (string): Username for a user
        password (string): Hashed password of a user
    """
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200, default="")
    cookie = models.CharField(max_length=400, default="")
