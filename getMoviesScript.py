import pickle
import pandas as pd
import sys


loadedModel = pickle.load(open('moviePickleFile', 'rb'))
movie = sys.argv[1]

df2 = pd.read_csv("40k_movies_df")
df2.drop(columns = "Unnamed: 0", inplace = True)

df2_feat = pd.read_csv("40k_movies_df_feat")
df2_feat.drop(columns = "Unnamed: 0", inplace = True)

loc = list(df2['Title']).index(movie)
list_recom_movies = list(loadedModel.kneighbors([df2_feat.iloc[loc]])[1])
c = 0
finalFetchedMovies = []
for i in list_recom_movies[0]:
    if (c>0):
        finalFetchedMovies.append(df2.at[int(i), 'Title'])
    c=c+1

print(finalFetchedMovies)
