  
# This code is an exercise done at module 5 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to format feature information, create new usefull features, and create a recommendation system 
# for users based on their own preview rated movies.

import zipfile
import pandas as pd
import numpy
import os

os.chdir('C:/Users/arthu/Downloads')
zf = zipfile.ZipFile('moviedataset.zip')
movies_df = pd.read_csv(zf.open('ml-latest/movies.csv'))
rating_df = pd.read_csv(zf.open('ml-latest/ratings.csv'))

print(movies_df.head())
movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))', expand=False)
movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)', expand=False)
movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df['genres'] = movies_df.genres.str.split('|')
print(movies_df.head())

moviesWithGenres = movies_df.copy()
for index, row in movies_df.iterrows():
    for genre in row['genres']:
        moviesWithGenres.at[index, genre] = 1
moviesWithGenres = moviesWithGenres.fillna(0)
print(moviesWithGenres.head())

rating_df.drop('timestamp', axis=1, inplace=True)

userInput = [
            {'title':'Breakfast Club, The', 'rating':5},
            {'title':'Toy Story', 'rating':3.5},
            {'title':'Jumanji', 'rating':2},
            {'title':"Pulp Fiction", 'rating':5},
            {'title':'Akira', 'rating':4.5}
         ] 
inputMovies = pd.DataFrame(userInput)
inputID = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]
inputMovies = pd.merge(inputID, inputMovies)
inputMovies = inputMovies.drop('year', axis=1).drop('genres', axis=1)
userMovies = moviesWithGenres[moviesWithGenres['title'].isin(inputMovies['title'].tolist())]
userMovies = userMovies.reset_index(drop=True)
userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
genreTable = moviesWithGenres.set_index(moviesWithGenres['movieId'])
genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

recommendatioTable = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
recommendatioTable.sort_values(ascending=False, inplace=True)
print(movies_df.loc[movies_df['movieId'].isin(recommendatioTable.head(20).keys())])
