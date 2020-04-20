#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
        """Return a body response containing string Hello HBNB!"""
        return 'Hello HBNB!'

if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
