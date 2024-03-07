#!/usr/bin/python3
"""
This module implements a basic Flask application.
"""

from flask import Flask

app = Flask(__name__)
# creates a Flask application in the current Python module


@app.route('/', strict_slashes=False)
# maps the specific URL with the assoiated function.
def hello():
    """
    A simple view function that returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    # Start the Flask app, accessible from any IP on port 5000
    app.run(host='0.0.0.0', port=5000)
