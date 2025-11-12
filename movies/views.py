from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Link, Rating
from .serializers import *
from django.db.models import F

from django.db.models import Q


#  N+1 Problem 
# waiting time 5.41 s in postman
import cProfile, io, pstats

class MovieLinkAPIView(APIView):
    def get(self, request):
        pr = cProfile.Profile()
        pr.enable()

        movies = Movie.objects.select_related('link').values_list(
            'movieId', 'title', 'genres', 'link__imdbId', 'link__tmdbId'
        )
        result = list(movies)

        pr.disable()
        s = io.StringIO()
        pstats.Stats(pr, stream=s).sort_stats('cumtime').print_stats(10)
        print(s.getvalue())  # appears in terminal
        return Response(result)



class RatingMovieAPIView(APIView):

    def get(self, request):
        ratings = Rating.objects.all() 
        data = []
        for r in ratings:
            data.append({
                'userId': r.userId,
                'rating': str(r.rating),
                'movie_title': r.movie.title, 
                'movie_genres': r.movie.genres,
            })
        return Response(data)
    

# solve
# waiting 272 ms with postman

class MovieLinkAPIView(APIView):

    def get(self, request):
        # movies = Movie.objects.select_related('link').all() 
        # serializer = MovieLinkSerializer(movies, many=True)
        # return Response(serializer.data)


        # return as tuple
        movies = Movie.objects.select_related('link').values_list(
            'movieId', 'title', 'genres', 'link__imdbId', 'link__tmdbId'
        )
        return Response(movies)

class RatingMovieAPIView(APIView):

    def get(self, request):
        ratings = Rating.objects.select_related('movie').all()
        serializer = RatingMovieSerializer(ratings, many=True)
        return Response(serializer.data)


class MovieFilterQAPIView(APIView):
    def get(self, request):
        moviesFiltered = Movie.objects.filter(Q(genres__icontains='Action') | Q(genres__icontains='Comedy'))
        serializer = MovieFilterSerializer(moviesFiltered, many=True)
        return Response(serializer.data)


class MovieUpdateAPIView(APIView):
    def patch(self,request):
        Movie.objects.filter(genres="Animation").update(genres="anime")
        return Response({"message": "update done"})
    
class MoveOnlyAPIView(APIView):
    def get(self,request):
        # movies = Movie.objects.only('genres') # as query set
        movies = Movie.objects.only('genres').values('genres') # as dict
        serializer = MovieOnlySerializer(movies, many =True)
        return Response(serializer.data)
    

class MovedeferAPIView(APIView):
    def get(self,request):
        movies = Movie.objects.defer('genres')
        movies = Movie.objects.defer('genres').values_list('genres')
        serializer = MoviedeferSerializer(movies, many =True)
        return Response(serializer.data)

# 210 ms in silk
class RatingByIndexedAPIView(APIView):
    def get(self, request):
        value = request.query_params.get('rating', 4.5)
        ratings = Rating.objects.filter(rating=value).values('userId', 'movie_id', 'rating')
        return Response(list(ratings))

# 255 ms in silk
class RatingByNonIndexedAPIView(APIView):
    def get(self, request):
        
        timestamp_gt = int(request.query_params.get('timestamp_gt', 1000000000))
        ratings = Rating.objects.filter(timestamp__gt=timestamp_gt).values('userId', 'movie_id', 'timestamp')
        return Response(list(ratings))
