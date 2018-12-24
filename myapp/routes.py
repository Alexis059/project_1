from myapp import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Alexis'}
	return '''
<html>
	<head>
		<title>Home page - Project 1</title>
	</head>
	<body>
		<h1>Hello, ''' + user['username'] + '''!</h1>
	</body>
</html>'''
