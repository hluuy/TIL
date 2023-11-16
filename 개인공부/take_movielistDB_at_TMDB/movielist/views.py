from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
import requests
from .models import Movie
# Create your views here.
def get_movie_data(request):
    api_key = '8fbda498ce79ea454eec38fe2012ea37'
    url = f'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return HttpResponseNotFound('Movie not found')
    
def save_movie_data(movie_id):
    movie_data = get_movie_data(movie_id)
    if movie_data:
        movie = Movie(
            title=movie_data['title'],
            release_date=movie_data['release_date'],
            overview=movie_data['overview'],
            vote_average=movie_data['vote_average']
        )
        movie.save()

def get_movie_datas(request):
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=8fbda498ce79ea454eec38fe2012ea37&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
    
    return JsonResponse({'movies': total_data})