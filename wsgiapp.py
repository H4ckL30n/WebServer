def app(environ, start_response):
	""" A bardebones WSGI application.

	This is a starting point for your own Web framework
	"""
	status = '200 OK'
	response_headers = [('Content-Type', 'text/plain')]
	start_response(status, resonse_headers)
	return [b'Hello world from a simple WSGI application']
