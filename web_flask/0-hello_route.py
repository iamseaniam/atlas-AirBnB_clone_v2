#!/usr/bin/python3
"""
This module implements a basic Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/strict_slashes=False')
def hello():
    """
    A simple view function that returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')
