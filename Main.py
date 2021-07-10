import pandas as pd
import matplotlib.pyplot as plt

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {
    "years":years, 
    "durations":durations
    }
#print(movie_dict)

durations_df = pd.DataFrame(movie_dict)
#print(durations_df)

#A visual inspection of our data
figure = plt.figure()
plt.plot(durations_df, durations)
plt.title('Netflix Movie Durations 2011-2020')
plt.show()

#Loading the rest of the data from a CSV
netflix_df = pd.read_csv("datasets/netflix_data.csv")
netflix_df[0:5]

#Filtering the movies
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
netflix_movies_col_subset[0:5]

#Creating a scatter plot
fig = plt.figure(figsize=(12,8))
plt.scatter(years, durations)
plt.title("Movie Duration by Year of Release")
plt.show()

#Digging the data deeper
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
short_movies[0:20]

#Marking non-feature films
colors = []

for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

#creating a more styled graph
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(years, durations)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

# This was just a little fun explotary analysis of some entertainment data I came accross to see if movies are getting shorter and I came to the conclusion that they are.