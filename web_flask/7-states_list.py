#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage, State

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


@app.route('/python', defaults={'string': 'is_cool'})
@app.route('/python/<string>')
def python(string='is_cool'):
        """Return a body response containing a string with the value
        of variable passed to the URL"""
        return 'Python %s' % escape(string.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
        """Displays a body response only if type of n is integer"""
        return '%i is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
        """Display a number template"""
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_od(n):
        """Display a number template"""
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def states():
        """Displays a body response with a
        list of all states sorted from A->Z"""
        states = storage.all(State)
        new_states = []
        for state in states:
                new_states.append([states[state].name, states[state].id])
        new_states.sort()
        return render_template('7-states_list.html', data=new_states)


@app.teardown_appcontext
def close(self=None):
        """remove the current SQLAlchemy Session"""
        storage.close()


if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
