from django.urls import path
from .views import *
urlpatterns = [
    path('cache-data/', CacheDataView.as_view()),
    path('cache-view/', CachedView.as_view()),
    path('cache-sql/', CachedSQLView.as_view()),
    path('cache-template/', CacheTemplateView.as_view()),
]
