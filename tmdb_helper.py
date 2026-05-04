import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

print("API KEY:", TMDB_API_KEY)

def search_movies(query):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }

    response = requests.get(url, params=params)

    print(response.json())

    data = response.json()

    return data.get("results", [])


def get_poster(poster_path):

    if poster_path is None:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"