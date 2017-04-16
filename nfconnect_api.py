#!/usr/bin/env python3
"""
    nfconnect_api.py
    Ethan Cassel-Mace, 15 April 2017

    Backend API for the nfconnect app. API manages database of users, rides, and serves ride information for a
    variety of queries.
"""
import flask
from flask import Flask, jsonify
import sys
import json

app = Flask(__name__)
TEST_VALUES = True

@app.route('/')
def say_hi():

    htmlStr = '<html lang="en">' + \
              '<head>' + \
              '  <title>Welcome to the NFConnect API</title>' + \
              '</head>' + \
              '<body>' + \
              '  <h1>Welcome to the NFConnect API</h1>' + \
              '  <p>Developed by Ethan Cassel-Mace and Erik Lagerquist for the NFConnect App.</p>' + \
              '</body>' + \
              '</html>'
    return htmlStr

#########################################################################
# User database routes:
#########################################################################

@app.route('/users/all/')
def get_user_by_username(username):
    if TEST_VALUES:
        users =[{'id': 1, 'username': 'lagerquiste', 'points': 99, 'num_trips_completed': 2, 'completed_trips': [0,3,4],
                 'upcoming_trips': [1, 7], 'registered_driver': False}, {'id': 0, 'username': 'casselmacee',
                 'points': 100, 'num_trips_taken': 2, 'completed_trips': [0,3,4], 'upcoming_trips': [1, 7],
                 'registered_driver': True}]
    else:
        pass

    return jsonify(result)


@app.route('/users/username/<username>')
def get_user_by_username(username):
    if TEST_VALUES:
        result = {'id': 0, 'username': 'casselmacee', 'points': 100, 'num_trips_taken': 2, 'trips_taken': [0,3,4],
                  'registered_driver': True}
    else:
        pass

    return jsonify(result)

@app.route('/users/id/<id>')
def get_user_by_username(id):
    if TEST_VALUES:
        result = {'id': 0, 'username': 'casselmacee', 'points': 100, 'num_trips_taken': 2, 'trips_taken': [0,3,4],
                  'registered_driver': True}
    else:
        pass

    return jsonify(result)




#########################################################################
# Rides database routes:
#########################################################################









if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
