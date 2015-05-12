from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello2')
@app.route('/hello2/<name>')
def hello_world2(name = 'Flask'):
    return '<h1>Hello, %s (2) !!</h1>' %name

if __name__ == '__main__':
	app.debug = True
	app.run()
