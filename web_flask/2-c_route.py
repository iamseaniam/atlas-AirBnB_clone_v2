#!/usr/bin/python3
"""
comment    
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ A simple view function that returns 'Hello HBNB!' """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A simple view function that returns 'HBNB!' """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ A simple view function that returns 'C %' """
    if text in c:
        text = text[1:-1].replace('_', ' ')
    return 'C %s' % text


if __name__ == 'Main':
    app.run(debug=True, host='0.0.0.0', port=5000)
