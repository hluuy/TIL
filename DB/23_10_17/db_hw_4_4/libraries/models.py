from django.db import models
from accounts.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)