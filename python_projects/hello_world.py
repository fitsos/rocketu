
from bottle import request, response, route, run

import blackjack

@route('/<name>')
def hello(name):
	import ipdb;ipdb.set_trace()
	hand = game.deal()
	response.set_cookie("hand", hand)

run(host='0.0.0.0', port=8080)

