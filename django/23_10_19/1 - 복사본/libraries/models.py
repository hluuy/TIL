from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True)
    adult = models.BooleanField(null=True)


    def __str__(self):
        return f"책 제목 : {self.title}"