from rest_framework import serializers
from .models import Movie, Link, Rating

class MovieLinkSerializer(serializers.ModelSerializer):
    imdbId = serializers.IntegerField(source='link.imdbId', read_only=True)
    tmdbId = serializers.IntegerField(source='link.tmdbId', read_only=True)

    class Meta:
        model = Movie
        fields = ['movieId', 'title', 'genres', 'imdbId', 'tmdbId']


class RatingMovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='movie.title', read_only=True)
    genres = serializers.CharField(source='movie.genres', read_only=True)

    class Meta:
        model = Rating
        fields = ['userId', 'rating', 'timestamp', 'title', 'genres']


class MovieFilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['movieId', 'title', 'genres']


class MovieOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['genres']


class MoviedeferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movieId', 'title']


    