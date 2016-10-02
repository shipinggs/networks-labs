from flask import Flask, request, json, jsonify, Response
from auth import *
from data import *

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome to the Cinema\n'


@app.route('/halls', methods=['GET'])
def api_halls():
    if request.method == 'GET':
        return jsonify(halls)


@app.route('/movies', methods=['GET'])
def api_movies():
    return jsonify(movies)


@app.route('/movies/<int:movieID>', methods=['GET'])
def api_movie(movieID):
    if request.method == 'GET':
        return jsonify(movies[movieID])

    elif request.method == 'POST':
        movie = movies[movieID]
        data = request.json


@app.route('/movies/<int:movieID>/<int:showtime>', methods=['GET', 'POST'])
def api_showtime(movieID, showtime):
    movie = movies[movieID]
    movieShowTime = movie['showtimes'][str(showtime)]

    if request.method == 'GET':
        return jsonify(movieShowTime)

    elif request.method == 'POST':
        data = request.json
        return api_purchase_ticket(data, movieShowTime)


@requires_auth
def api_purchase_ticket(data, movieShowTime):
    if movieShowTime['seats-taken'] < halls[movieShowTime['hall']]['capacity']:
        seat = movieShowTime['seats-taken'] + 1
        movieShowTime['seats-taken'] = seat
        movieShowTime['ticket-holders'][seat] = data["name"]
        return jsonify(movieShowTime)
    else:
        return 'There are no seats available for this movie at this time\n'


if __name__ == '__main__':
    app.run(debug=True)
