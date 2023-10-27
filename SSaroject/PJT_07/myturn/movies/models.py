from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100) # 배우 이름

    def get_movies(self):
        return self.movies.all().values_list('title', flat=True)

class Movie(models.Model):
    title = models.CharField(max_length=100) # movie title
    overview = models.TextField() # movie plot
    release_date = models.DateTimeField(default='') # movie release date
    poster_path = models.TextField() # poster file path
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    def get_actors(self):
        return self.actors.all().values_list('name', flat=True)
    
    def get_review_set(self):
        return self.review_set.all().values('title', 'content')

class Review(models.Model):
    title = models.CharField(max_length=100) # review title
    content = models.TextField() # review content
    movie = models.ManyToManyField(Movie)

    def get_movie(self):
        return self.movie.all().values_list('title', flat=True)