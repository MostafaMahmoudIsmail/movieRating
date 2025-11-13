from django.urls import path
from .views import *

urlpatterns = [
    path('run-sleep/', RunSleepTaskView.as_view()),
    path('run-calc/', RunCalcTaskView.as_view()),
]
