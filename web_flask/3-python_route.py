#!/usr/bin/python3
"""comment"""

from flask import Flask

app = Flask(__name__)


app.route('/', strict_slashes=False)
def hello():
    """comment"""
    return 'Hello HBNB!'


app.route('/hbnb', strict_slashes=False)
def hbnb():
    """comment"""
    return 'HBNB'


app.route('/c/<text>', strict_slashes=False)
def c(text):
    """comment"""
    text.replace("_", " ")
    return 'C %' % text


app.route('/python/<text>', strict_slashes=False)
def python(text):
    """comment"""
    text = 'id cool'
    text.replace("_", " ")
    return 'Python %' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
