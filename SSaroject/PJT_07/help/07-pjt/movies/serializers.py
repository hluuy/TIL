from rest_framework import serializers
from .models import Actor, Movie, Review

class MovieTitleSrializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSrializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content')
        
class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializerForMovie(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    actors = ActorSerializerForMovie(many=True)
    review_set = ReviewListSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSrializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'