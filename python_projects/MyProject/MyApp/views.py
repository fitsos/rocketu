# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import random

def home(request):
	if request.session.get("counter") is not None:
		request.session["counter"] += 1
	else:
		request.session["counter"] = 0
	return HttpResponse(str(request.session["counter"]))

def say_hello(request, name):
	# return HttpResponse('Hello {}'.format(name))
	data = {"name": name}
	response = render_to_response('home.html',data)
	return response

count = 0
def counter(request):
	global count
	count += 1
	data = { 'count': count }
	return render_to_response('home.html', data)

def test(request):
	if request.session.get("hands") is not None:
		return HttpResponse(str(request.session["hands"]))
	else:
		request.session["hands"] = tuple(two_el())
		return HttpResponse(str(request.session["hands"]))

def rand13():
	for i in range(0, 14): 
		# print i
		num = random.randint(0, 53)
		# print num
		array = []
		array.append(num)
		# print array
		return array

def two_el():
		# print rand13(), rand13()
		return rand13(), rand13()

def ifelse(request, name=''):
	data = {
		'player': {
			'name': name
		}
	}
	response = render_to_response('ifelse.html', data)
	return response

def blackjack(request):
	# return HttpResponse("Through!")
	deck = []
	for suit in ['H', 'C', 'D', 'S']:
		for n in range(1, 14):
			deck.append((suit, n))
	data = { 'deck': deck }
	response = render_to_response('blackjack.html', data)
	return response

