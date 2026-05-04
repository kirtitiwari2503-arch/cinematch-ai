import streamlit as st
from tmdb_helper import search_movies, get_poster

# PAGE CONFIG
st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("🎥 CineMatch AI")

st.sidebar.markdown("""
### Features

✅ Real Movie Database  
✅ TMDB Integration  
✅ Live Search  
✅ Movie Posters  
✅ Modern UI
""")

# MAIN TITLE
st.title("🎬 CineMatch AI")

st.markdown(
    "### Discover Movies Instantly 🍿"
)

st.write("")

# SEARCH INPUT
movie_name = st.text_input(
    "Search Any Movie"
)

# BUTTON
if st.button("Search 🚀"):

    if movie_name.strip() == "":

        st.warning("Please enter movie name")

    else:

        with st.spinner("Searching movies..."):

            movies = search_movies(movie_name)

        if not movies:

            st.error("No movies found")

        else:

            st.subheader("🎯 Search Results")

            cols = st.columns(5)

            for col, movie in zip(cols, movies[:10]):

                with col:

                    poster = get_poster(
                        movie.get("poster_path")
                    )

                    if poster:

                        st.image(
                            poster,
                            use_container_width=True
                        )

                    st.success(
                        movie.get("title")
                    )

                    st.caption(
                        movie.get(
                            "release_date",
                            "N/A"
                        )
                    )