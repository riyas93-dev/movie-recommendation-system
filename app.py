import streamlit as st
import pickle
import pandas as pd
import requests

# 1. UPDATED: Function to fetch the movie poster using headers and a Bearer token
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    
    # read access token
    bearer_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWIxZDM4MmY1ODA4M2Y3YmVlYWJmNzdiNmVhNjJlOSIsIm5iZiI6MTc4MzQ3OTUxMC42NDUsInN1YiI6IjZhNGRiY2Q2ZjczOWU2NzgzZGY5MDI0OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z6v4ncgE7KIPz7avoeJcYBRsxrIMwJZ9VA9tDHAf_eM"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        #fetching the poster data from json response
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception as e:
        # Fallback placeholder if there's a connection issue or missing poster
        return "https://via.placeholder.com/500x750?text=No+Poster"

# 2. Load the saved model assets
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity_matrix.pkl', 'rb'))
movies_df = pd.DataFrame(movies)

# 3. Recommender function
def recommend(movie_name):
    movie_index = movies_df[movies_df['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    
    for i in movies_list:
        # Pull the movie ID
        movie_id = movies_df.iloc[i[0]].movie_id 
        
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters

# 4. Streamlit UI Elements
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Type or select a movie to get recommendations:',
    movies_df['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    
    # Create 5 columns side-by-side
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
        
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
        
    with col4:
        st.text(names[3])
        st.image(posters[3])
        
    with col5:
        st.text(names[4])
        st.image(posters[4])