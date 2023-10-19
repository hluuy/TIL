from django.db import models
import requests


# Create your models here.
class Library(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=50)
    isbn = models.TextField()
    pubdate = models.DateField(null=True, blank=True)
    pricesales = models.IntegerField(null=True)
    pricestandard = models.IntegerField(null=True)
    publisher = models.CharField(max_length=50)
    adult = models.BooleanField(default=False)

    @classmethod
    def insert_data(cls):
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbdudwns12891705002&QueryType=ItemNewAll&MaxResults=20&start=1&SearchTarget=Book&output=js&Version=20131101')
        data = response.json()


        for ls in data.get('item'):            
            library = cls(title=ls.get("title"), author=ls.get("author"), isbn=ls.get("isbn"), pubdate=ls.get("pubDate"), pricesales=ls.get("priceSales"), pricestandard=ls.get("priceStandard"), publisher=ls.get("publisher"), adult=ls.get("adult"))
            library.save()