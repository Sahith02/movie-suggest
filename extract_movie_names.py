import pandas as pd
import numpy as np

df = pd.read_csv('40k_movies_df')
all_movies = list(df['Title'])

#print(all_movies.count(np.nan))
print(all_movies[23606: 23608])

#import json 
  
# Data to be written 
#dictionary ={ 
#    "movies": all_movies
#} 
  
# Serializing json  
#json_object = json.dumps(dictionary, indent = 4) 
  
# Writing to sample.json 
#with open("sample.json", "w") as outfile: 
#    outfile.write(json_object) 


with open('movieList1.txt', 'w+') as f:
    f.write("[")
    for item in all_movies[23607:]:
        f.write('"%s", \n' %item)
    f.write("]")

print('Done!')
