from django.db import models
# from accounts.models import User
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    genre = models.CharField(max_length=250)
    score = models.FloatField(null=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)