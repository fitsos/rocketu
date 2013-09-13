# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from cars_app.models import CarChoice, Equipment


def see_cars(request):
    now = datetime.datetime.now()
    html = "<li> Your car: %s equipment: %s @ %s</li><br/>" % (CarChoice, Equipment, now)
    return HttpResponse(html)