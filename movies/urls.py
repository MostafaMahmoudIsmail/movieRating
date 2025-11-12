from django.urls import path
from .views import *

urlpatterns = [
    path('MovieLink/', MovieLinkAPIView.as_view()),
    path('RatingMovie/', RatingMovieAPIView.as_view()),
    path('movieFiltered/', MovieFilterQAPIView.as_view()),
    path('movieupdated/', MovieUpdateAPIView.as_view()),
    path('MovieOnly/', MoveOnlyAPIView.as_view()),
    path('Movedefer/', MovedeferAPIView.as_view()),
    
    path('ratings/indexed/', RatingByIndexedAPIView.as_view()),
    path('ratings/nonindexed/', RatingByNonIndexedAPIView.as_view()),

    

]
