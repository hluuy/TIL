from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre
# import request

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.get_genres()
    context = {
        'movie': movie,
        'genres': genres
        }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    pass
