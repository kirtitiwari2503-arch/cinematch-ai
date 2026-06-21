import streamlit as st
from tmdb_helper import search_movies, get_poster

# PAGE CONFIG
st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    padding: 12px;
}

.stButton button {
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #ff1f1f;
    color: white;
}

.css-1d391kg {
    background-color: #111111;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🎥 CineMatch AI")

st.sidebar.markdown("""
## About

CineMatch AI helps users discover movies instantly using live TMDB API integration.

### Features
- 🎬 Live Movie Search
- 🍿 Real Posters
- ⭐ Movie Release Dates
- 🚀 Fast Results
""")

# HERO SECTION
st.markdown("""
# 🎬 CineMatch AI

### Your Smart Movie Discovery Assistant 🍿
""")

st.write("")

# SEARCH BAR
movie_name = st.text_input(
    "Search your favorite movie"
)

# SEARCH BUTTON
if st.button("🔍 Search Movies"):

    if movie_name.strip() == "":

        st.warning("⚠️ Please enter a movie name")

    else:

        with st.spinner("Finding best movies for you..."):

            movies = search_movies(movie_name)

        if not movies:

            st.error("❌ No movies found")

        else:

            st.success(f"Showing results for: {movie_name}")

            st.write("")

            cols = st.columns(5)

            for index, movie in enumerate(movies[:10]):

                with cols[index % 5]:

                    poster = get_poster(
                        movie.get("poster_path")
                    )

                    st.image(
                        poster,
                        use_container_width=True
                    )

                    st.markdown(
                        f"### 🎥 {movie.get('title')}"
                    )

                    st.caption(
                        f"📅 Release: {movie.get('release_date', 'N/A')}"
                    )

                    rating = movie.get(
                        "vote_average",
                        "N/A"
                    )

                    st.write(
                        f"⭐ Rating: {rating}"
                    )

