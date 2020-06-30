from scripts.get_details_script import get_movie_details_from_index, get_movies, search_value
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
# import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_10_movies', methods=['POST'])
def predict_10_post():
    '''
    For rendering results on HTML GUI
    '''
    movie_searched = request.values.get('movie')
    return str(get_movies(movie=movie_searched))

@app.route('/get_n_movies', methods=['POST'])
def predict_n_post():
    '''
    For rendering results on HTML GUI
    '''
    movie_searched = request.values.get('movie')
    if('show' in request.values):
        show_n = int(request.values.get('show'))
    else:
        show_n = 25
    try:
        movies_recommended = get_movies(movie=movie_searched, show=show_n) + [{'imdb_id': 0, 'title': "That's all for now folks!", 'imdb_score': None, 'genre': [], 'poster_link': '', 'year': ''}]
        # return str(get_movies(movie=movie_searched, show=show_n))
        return render_template('display.html', movies = movies_recommended, movie_searched_for = movie_searched)
    except:
        return render_template('error.html')

@app.route('/search_for_movie', methods=['POST'])
def search_for_movie():
    # search = request.values.get('search')
    search = request.form['search']
    return jsonify(search_value(search))

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html'), 500


if __name__ == "__main__":
    app.run(debug=True)