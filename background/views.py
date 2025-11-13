from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .tasks import heavy_sleep_task, heavy_calculation_task
from celery.result import AsyncResult

class RunSleepTaskView(APIView):
    def get(self, request):
        task = heavy_sleep_task.delay()
        return Response({
            "message": f"task started for 10 seconds.",
        })

class RunCalcTaskView(APIView):
    def get(self, request):
        n = 1000
        task = heavy_calculation_task.delay(n)
        return Response({
            "message": f"Calculation task started with n={n}.",
        })

