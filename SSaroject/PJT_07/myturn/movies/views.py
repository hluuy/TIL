from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(requset, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(requset):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(requset, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(["GET"])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail(requset, review_pk):
    review = Review.objects.get(pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)