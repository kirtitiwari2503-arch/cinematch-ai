import requests
import os

# Get TMDB API key from environment variable
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


# Search movies from TMDB
def search_movies(query):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("results", [])


# Get movie poster
def get_poster(poster_path):

    if poster_path is None:
        return "https://via.placeholder.com/300x450?text=No+Image"

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
