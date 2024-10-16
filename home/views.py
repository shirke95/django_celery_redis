from django.http import HttpResponse

from .tasks import handle_sleep, add


# Create your views here.
def home(request):
    # time.sleep(20)
    handle_sleep.delay()
    add(3, 4)
    return HttpResponse("Hello From Celery")
