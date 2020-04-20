#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
        """Return a body response containing a string Hello HBNB!"""
        return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
        """Return a body response containing a string HBNB"""
        return 'HBNB'


@app.route('/c/<string>')
def c(string):
        """Return a body response containing
        a string with the value of variable passed to the URL"""
        return 'C %s' % escape(string.replace('_', ' '))

if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
