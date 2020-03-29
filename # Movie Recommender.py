# Movie Recommender 
# Author: Michael Keller
# Date: 3/1/2020
# for Python 3.7.6 

# Imports 
import xlrd
import os 
from os import path 
import numpy as np
import random
import pathlib
from pathlib import PureWindowsPath

##########################################################################################

# Find path
mpath = path.realpath("FavoriteMovies.csv")

# Sets working directory to path 
# os.chdir('c:/Users/Keller/Desktop/Learning/Projects/') <- this works but makes you manually set directory 
os.chdir(path.dirname(mpath))

# check to see if FavouriteMovies.csv exists 
if path.exists("FavoriteMovies.csv") == 0:
    print("Movie List can not be found,3 please download movie list or change directory.")

# open movie list 
import pandas as pd #makes function pandas called useing pd 
# problem below, says path does not exist - fixed by writing path, use / instead of \
df = pd.read_csv ('FavoriteMovies.csv')  

# removes title row from DataFrame - only needed if name is in first row and coloum 
# df = df.drop(df.index[0]) 

# More from dataFrame to array 
titles = [] 
ratings = []
genre = []
for i, row in df.iterrows():
    titles.append( row['Title'])
    ratings.append(row['Rating'])
    genre.append(row['Category'])

# remove spaces from list to make code more durable 
for i in range(len(genre)):
    genre[i] = genre[i].strip(' ')
index = list(range(0, len(titles)))

# incase I ever want to make this not have to import from favorite movies.csv, copy paste below printout into code 
#print(titles)
#print(ratings)
#print(genre)

##########################################################################################

# Find what type of movie the user wants to watch 
print('What type of movie would you like to watch?')
print('1  = Action')
print('2  = Adventure')
print('3  = Comedy')
print('4  = Coming of Age')
print('5  = Crime')
print('6  = Documentary')
print('7  = Horror')
print('8  = Musical')
print('9  = Noir')
print('10 = Psychological')
print('11 = Romance')
print('12 = Suspense')
print('13 = War')
choice = int(input('Chose a number: '))


# Logically index movies out of the list based on their choice
# create mask 
mask = []
if choice == 1:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Action')
elif choice == 2:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Adventure')
elif choice == 3:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Comedy')
elif choice == 4:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Coming of Age')
elif choice == 5:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Crime')
elif choice == 6:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Documentary')
elif choice == 7:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Horror')
elif choice == 8:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Musical')
elif choice == 9:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Noir')
elif choice == 10:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Psychological')
elif choice == 11:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Romance')
elif choice == 12:
    for i in range(len(genre)):
        mask.append(genre[i] == 'Suspense')
elif choice == 13:
    for i in range(len(genre)):
        mask.append(genre[i] == 'War')
else:
    print('I know what you did')
    mask = index
    
# apply mask 
locs = np.nonzero(mask)

# adjust for index
locs = locs[0]

while True:
    # Do they want to choose or have one selected 
    choice2 = input('Do you like free will? (Y/N) \n')

    if choice2 == 'Y':
        print('------------------ Movie List ----------------')
        print( 'Rating: Title')
        # Print list recommendations 
        for i in range(len(locs)):
            print(str(ratings[locs[i]])+ ': ' + titles[locs[i]]) 
        print('------------------ Movie List ----------------')
        break

    elif choice2 == 'N':
        print('------------------ Movie ----------------')
        movie = random.randrange(len(locs))
        movie = locs[movie]
        print(titles[movie])
        print('------------------ Movie ----------------')
        break

    else:
        print('Incorrect Input, try again')


