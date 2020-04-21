#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage, State, Amenity, City, Place, User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def full_airbnb():
        """ Dynamic Airbnb page """
        states = storage.all(State)
        amenities = storage.all(Amenity)
        cities = storage.all(City)
        places = storage.all(Place)
        users = storage.all(User)

        new_places = []
        amenities = [[amenities[amenity].name] for amenity in amenities]
        amenities.sort()
        states = [[states[state].name, states[state].id] for state in states]
        states.sort()
        cities = [[cities[city].name, cities[city].state_id]
                  for city in cities]
        cities.sort()

        for p in places:
                for user in users:
                        if (places[p].user_id == users[user].id):
                                n = users[user].first_name
                                l = users[user].last_name
                                new_places.append([places[p].name,
                                                   places[p].price_by_night,
                                                   places[p].max_guest,
                                                   places[p].number_rooms,
                                                   places[p].number_bathrooms,
                                                   n + " " + l,
                                                   places[p].description])

        new_places.sort()
        return (render_template('100-index.html', S=states, C=cities,
                                A=amenities, P=new_places))


@app.teardown_appcontext
def close(self=None):
        """remove the current SQLAlchemy Session"""
        storage.close()


if __name__ == "__main__":
        """Run by module"""
        app.run(host='0.0.0.0', port='5000')
