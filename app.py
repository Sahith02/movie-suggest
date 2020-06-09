import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
loadedModel = pickle.load(open('moviePickleFile', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_10_movies', methods=['POST'])
def predict_10_post():
    '''
    For rendering results on HTML GUI
    '''
    movie = request.values.get('movie')

    df2 = pd.read_csv("40k_movies_df")
    df2.drop(columns = "Unnamed: 0", inplace = True)

    df2_feat = pd.read_csv("40k_movies_df_feat")
    df2_feat.drop(columns = "Unnamed: 0", inplace = True)

    loc = list(df2['Title']).index(movie)
    list_recom_movies = list(loadedModel.kneighbors([df2_feat.iloc[loc]])[1])
    c = 0
    finalFetchedMovies = {}
    for i in list_recom_movies[0]:
        if (c>0):
            finalFetchedMovies[c] = df2.at[int(i), 'Title']
        c=c+1

    return str(finalFetchedMovies)

@app.route('/get_10_movies', methods=['GET'])
def predict_10_get():
    '''
    For rendering results on HTML GUI
    '''
    movie = request.values.get('movie')

    df2 = pd.read_csv("40k_movies_df")
    df2.drop(columns = "Unnamed: 0", inplace = True)

    df2_feat = pd.read_csv("40k_movies_df_feat")
    df2_feat.drop(columns = "Unnamed: 0", inplace = True)

    loc = list(df2['Title']).index(movie)
    list_recom_movies = list(loadedModel.kneighbors([df2_feat.iloc[loc]])[1])
    c = 0
    finalFetchedMovies = {}
    for i in list_recom_movies[0]:
        if (c>0):
            finalFetchedMovies[c] = df2.at[int(i), 'Title']
        c=c+1

    return str(finalFetchedMovies)
if __name__ == "__main__":
    app.run(debug=True)