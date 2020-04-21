#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage, State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def only_states():
        """ send all states
        """
        states = storage.all(State)
        states = [[states[s].id, states[s].name] for s in states]
        states = sorted(states, key=lambda x: x[1])
        return (render_template('9-states.html', S=states, C=None, F=3))


@app.route('/states/<id>')
def city_of_state_id(id):
        """ cities of state id
        """
        new = []
        flag = 0
        states = storage.all(State)
        for s in states:
                if (id == states[s].id):
                        flag = 1
                        new.append((states[s].id, states[s].name))
        if (flag == 0):
                return (render_template('9-states.html', S=None, C=None, F=0))
        states = storage.all(City)
        cities = []
        for city in states:
                if (states[city].state_id == new[0][0]):
                        cities.append((states[city].id, states[city].name))
        cities = sorted(cities, key=lambda x: x[1])
        return (render_template('9-states.html', S=new, C=cities, F=1))


@app.teardown_appcontext
def close(self=None):
        """remove the current SQLAlchemy Session"""
        storage.close()


if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
