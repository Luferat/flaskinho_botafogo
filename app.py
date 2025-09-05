from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!<p>Que legal!</p>'


@app.route('/about')
def about():
    return 'Sobre...'


if __name__ == '__main__':
    app.run(debug=True)