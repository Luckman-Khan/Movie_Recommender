import streamlit as st
import pickle
import pandas as pd
import requests



def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[movie_index])), reverse=True,key= lambda x:x[1])
  recommended_movie_names = []


  for i in distances[1:6]:
      movie_id = movies.iloc[i[0]].movie_id
      recommended_movie_names.append(movies.iloc[i[0]].title)
  return recommended_movie_names

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

print(movies_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select an option',movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
     st.write(i)