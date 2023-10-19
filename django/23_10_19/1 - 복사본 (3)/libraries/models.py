from django.db import models

# Create your models here.
class Library(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.IntegerField(null=True)
    pubdate = models.DateField(null=True, blank=True)
    pricesales = models.IntegerField(null=True)
    pricestandard = models.IntegerField(null=True)
    publisher = models.CharField(max_length=50)
    bestrank = models.IntegerField(null=True)