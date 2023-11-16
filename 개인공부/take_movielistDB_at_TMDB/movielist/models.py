from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    overview = models.TextField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    # 기타 필요한 필드 추가