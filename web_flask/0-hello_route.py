#!/usr/bin/python3
from flask import Flask
"""documentaion"""
app = Flask(__name__)


@app.route('/strict_slashes=False')

def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
