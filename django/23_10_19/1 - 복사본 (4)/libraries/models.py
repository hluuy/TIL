from django.db import models
import requests

# Create your models here.
class Library(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.IntegerField(default=0)
    pubdate = models.DateField(null=True, blank=True)
    pricesales = models.IntegerField(default=0)
    pricestandard = models.IntegerField(default=0)
    publisher = models.CharField(max_length=50)
    bestrank = models.IntegerField(default=0)

    @classmethod
    def insert_data(cls):
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=[ttbdudwns12891705001]&QueryType=ItemNewAll&MaxResults=20&start=1&SearchTarget=Book&output=js&Version=20231015')
        data = response.json()

        for item in data:
            library = cls(title=item['title'], author=item['author'], isbn=item['isbn'], pubdate=item['pubDate'], pricesales=item['priceSales'], pricestandard=['priceStandard'], publisher=item['publisher'], bestrank=item['bestRank'])
            library.save()