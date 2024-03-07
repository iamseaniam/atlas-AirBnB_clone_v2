#!/usr/bin/python 3
"""
comment    
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C %s' % text

if __name__ == 'Main':
    app.run(debig=True, host='0.0.0.0', port=5000)
