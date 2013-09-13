__author__ = 'fitsos'

# from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests



def money(requests):
    # url = "http://www.cnet.com/"
    url = "http://bootcamp-rocketu.rhcloud.com/exercises/moviepicker/assets/data/movies.json"
    data = requests.get(url)
    # cache.set(url, data, 300)
    # cached_data = cache.GET(url)
    render(requests, 'money.html', data)
    #return HttpResponse(data)
