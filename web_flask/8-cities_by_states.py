#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage, State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
        """Displays a body response with a
        list of all states sorted from A->Z"""
        states = storage.all(State)
        cities = storage.all(City)
        states = [[states[s].name, states[s].id] for s in states]
        cities = [[cities[c].name, cities[c].state_id, cities[c].id]
                  for c in cities]

        cities.sort()
        states.sort()

        return (render_template('8-cities_by_states.html', S=states, C=cities))


@app.teardown_appcontext
def close(self=None):
        """remove the current SQLAlchemy Session"""
        storage.close()


if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
