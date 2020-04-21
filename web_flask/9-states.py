#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage, State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
        """Displays a body response with a
        list of all states sorted from A->Z"""
        states = storage.all(State)
        states = [[states[s].name, states[s].id] for s in states]
        states.sort()
        return render_template('9-states.html', S=states, F=0)


@app.route('/states/<id>')
def list_states(id):
        """Displays a body response with a
        list of all states sorted from A->Z"""
        states = storage.all(State)
        cities = storage.all(City)
        flag = 0
        new = []
        for s in states:
                if (id == states[s].id):
                        flag = 1
                        new.append([states[s].id, states[s].name])
        if (flag == 0):
                return (render_template('9-states.html', S=None, C=None, F=0))
        city = []
        for c in cities:
                if (cities[c].state_id == new[0][0]):
                        city.append([cities[c].id, cities[c].name])
        city.sort()
        return (render_template('9-states.html', S=new, C=city, F=1))


@app.teardown_appcontext
def close(self=None):
        """remove the current SQLAlchemy Session"""
        storage.close()


if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
