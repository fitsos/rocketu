import logging
from bottle import request, route, run

@route('/log/<name>')
def index(name='Anonymous'):
	level = int(request.query.levelno)
	print name.upper(),
	print logging.getLevelName(level),
	print request.query.msg
	return 'OK'

# @route('/pledge/<userid>')
# def set_pledge(userid):
# 	user = get_user(user_id)
# 	pledge_amount = int(request.query.pledge)
# 	user.set_pledge_amount(pledge_amount)
# 	return "OK" #JSON Object return {status: true }

run (host='localhost', port=8080)