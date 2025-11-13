from django.shortcuts import render
import time
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie


def heavy_computation():
    time.sleep(5)
    return "Computation Complete"



class CacheDataView(APIView):
    def get(self, request):
        data = cache.get('heavy_data')

        if not data:
            data = heavy_computation()
            cache.set('heavy_data', data, timeout=60 * 15)
            return Response({'data Without Cache': data})

        return Response({'data From Cache': data})



@method_decorator(cache_page(60 * 5), name='dispatch')
class CachedView(APIView):
    def get(self, request):
        data = heavy_computation()
        return Response({'data': data})



class CachedSQLView(APIView):
    def get(self, request):
        data = cache.get('sql_data')

        if not data:
            data = list(Movie.objects.all().values())
            cache.set('sql_data', data, timeout=60 * 10)
            return Response({'data Without Cache': data})

        return Response({'data With Cache': data})



class CacheTemplateView(APIView):
    def get(self, request):
        categories = ["Phones", "Laptops", "Accessories", "Tablets", "Cameras"]
        return render(request, "cached_template.html", {"categories": categories})
