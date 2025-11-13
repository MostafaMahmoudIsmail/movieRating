from celery import shared_task
import time

@shared_task
def heavy_sleep_task():
    seconds = 10
    time.sleep(seconds)
    return f"Finished sleeping for {seconds} seconds."

@shared_task
def heavy_calculation_task(n):
    time.sleep(5) 
    total = 0
    for i in range(n):
        total += i
    return f"Calculation of {n}M loops done. Total = {total}"


@shared_task
def scheduled_3min_task():
    print("Running scheduled task every 3 minutes")
    return "Task executed every 3 minutes"

