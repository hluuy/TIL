from rest_framework import serializers
from rest_framework import relations
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    def get_movies(self, obj):
        return obj.get_movies()
    
    class Meta:
        model = Actor
        fields = ('name', 'movies')

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    review_set = serializers.SerializerMethodField()
    def get_actors(self, obj):
        return obj.get_actors()
    
    def get_review_set(self, obj):
        return obj.get_review_set()

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path')
    # actors = serializers.Nested(ActorSerializer, many=True, fields=('name',))

    # class Meta:
    #     model = Movie
    #     fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    def get_movie(self, obj):
        return obj.get_movie()
    
    class Meta:
        model = Review
        fields = ('movie', 'title', 'content')