# This code is an exercise done at module 5 as part of the course (ML0101EN) Machine Learning with Python_A Practical Introduction by IBM.
# The intention of the exercise is to create a recommendation system for users based on rates from users with similar movie taste.

import zipfile
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

os.chdir('C:/Users/arthu/Downloads')
zf = zipfile.ZipFile('moviedataset.zip')
movies_df = pd.read_csv(zf.open('ml-latest/movies.csv'))
rating_df = pd.read_csv(zf.open('ml-latest/ratings.csv'))

rating_df.drop('timestamp', axis=1, inplace=True)
movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))')
movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)')
movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df['genres'] = movies_df.genres.str.split('|')
movies_df.drop('genres', axis=1, inplace=True)
print(movies_df.head())

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
inputMovies.drop('year', axis=1, inplace=True)
userSubset = rating_df[rating_df['movieId'].isin(inputMovies['movieId'].tolist())]
userSubsetGroup = userSubset.groupby(['userId'])
userSubsetGroup = sorted(userSubsetGroup, key=lambda x: len(x[1]), reverse=True)

userSubsetGroup = userSubsetGroup[0:100]
pearsonCorralationDict = {}
for name, group in userSubsetGroup:
    group = group.sort_values(by='movieId')
    inputMovies = inputMovies.sort_values(by='movieId')
    nRatings = len(group)
    temp_df = inputMovies[inputMovies['movieId'].isin(group['movieId'].tolist())]
    tempRatingList = temp_df['rating'].tolist()
    tempGroupList = group['rating'].tolist()
    Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList), 2) / (float(nRatings))
    Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList), 2) / (float(nRatings))
    Sxy = sum( i * j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/(float(nRatings))
    if Sxx != 0 and Syy != 0:
        pearsonCorralationDict[name] = Sxy / sqrt(Sxx * Syy)
    else:
        pearsonCorralationDict[name] = 0
pearsonDF = pd.DataFrame.from_dict(pearsonCorralationDict, orient='index')
pearsonDF.columns = ['similarityIndex']
pearsonDF['userId'] = pearsonDF.index
pearsonDF.index = range(len(pearsonDF))

topUsers = pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]
topUsersRatings = topUsers.merge(rating_df, right_on='userId', left_on='userId', how='inner')
topUsersRatings['weightedRatings'] = topUsersRatings['similarityIndex'] * topUsersRatings['rating']
tempTopUsersRating = topUsersRatings.groupby('movieId').sum()[['similarityIndex', 'weightedRatings']]
tempTopUsersRating.columns = ['sum_similarityIndex', 'sum_weightedRating']
recommendation_df = pd.DataFrame()
recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
recommendation_df['movieId'] = tempTopUsersRating.index
recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
print(movies_df.loc[movies_df['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())])
