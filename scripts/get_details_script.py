import numpy as np
import pandas as pd
import pickle

# loading model and data files
model_filename = "./model/KNN_MODEL_V2.0_ENGINE.pickle"
df_clean_file_name = "./data/DATA_V2.0_CLEAN_DF.pickle"
df_clean_features_file_name = "./data/DATA_V2.0_CLEAN_FEATURES.npy"
loaded_model = pickle.load(open(model_filename, 'rb'))
df_clean = pd.read_pickle(df_clean_file_name)
df_clean_features = np.load(df_clean_features_file_name)

def get_movie_details_from_index(index):
    movie_details = dict()
    movie_details_raw = df_clean.iloc[index]
    movie_details["imdb_id"] = movie_details_raw['imdbId']
    movie_details["title"] = movie_details_raw['Title']
    movie_details["imdb_score"] = movie_details_raw['IMDB Score']
    movie_details["genre"] = movie_details_raw['Genre'].split('|')
    movie_details["poster_link"] = movie_details_raw['Poster']
    if(int(movie_details_raw['year']) == movie_details_raw['year']):
        movie_details["year"] = int(movie_details_raw['year'])
    else:
        movie_details["year"] = 0
    return movie_details

def get_movies(movie, show = 10):
    index = np.where(df_clean['Title'] == movie)[0][0]
    recommends = loaded_model.kneighbors([df_clean_features[index]], return_distance = False, n_neighbors = show + 1)[0]
    return str([get_movie_details_from_index(i) for i in recommends if index != i][:show])

def search_value(search):
    search = search.lower()
    return {"movies": [x for x in df_clean['Title'] if x.lower().startswith(search)][:10]}
