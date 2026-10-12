from urllib import response

import pickle
import pandas as pd
import requests
import streamlit as st

import gzip
import pickle
import os

api_key = st.secrets["TMDB_API_KEY"]



def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommeded_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommeded_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommeded_movies, recommended_movies_posters



movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)




parts = ["similarity_part1.bin", "similarity_part2.bin"]
compressed_file = "similarity_lossless.pkl.gz"

with open(compressed_file, "wb") as output:
    for part_name in parts:
        with open(part_name, "rb") as part:
            output.write(part.read())

with gzip.open(compressed_file, "rb") as f:
    similarity = pickle.load(f)





# ---------- CINEMATCH FRONTEND ----------
# Keep only ONE st.set_page_config() in your app.
# If one already exists, update it instead of adding another.

st.markdown("""
<style>
    .stApp {
        background-color: #FAF9F6;
        color: #292824;
    }

    .block-container {
        max-width: 1120px;
        padding-top: 2rem;
        padding-bottom: 2.5rem;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .brand {
        font-size: 20px;
        font-weight: 750;
        letter-spacing: -0.6px;
        color: #292824;
    }

    .brand-accent {
        color: #874A50;
    }

    .eyebrow {
        color: #874A50;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.8px;
        margin-bottom: 12px;
    }

    .hero-title {
        color: #292824;
        font-size: clamp(34px, 4vw, 48px);
        font-weight: 750;
        letter-spacing: -1.8px;
        line-height: 1.15;
        margin: 20px 0 12px 0;
    }

    .hero-copy {
        color: #77746E;
        font-size: 15px;
        line-height: 1.8;
        max-width: 650px;
    }

    .section-heading {
        color: #292824;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    .section-copy {
        color: #77746E;
        font-size: 14px;
    }

    div[data-baseweb="select"] > div {
        background: #FFFFFF;
        border: 1px solid #DFDCD5;
        border-radius: 7px;
        min-height: 46px;
    }

    .stButton > button {
        background: #874A50;
        color: #FFFFFF;
        border: 1px solid #874A50;
        border-radius: 7px;
        min-height: 44px;
        font-weight: 600;
        transition: background 0.15s ease;
    }

    .stButton > button:hover {
        background: #713B41;
        border-color: #713B41;
        color: #FFFFFF;
    }

    [data-testid="stImage"] img {
        border-radius: 6px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 8px;
    }

    hr {
        border-color: #E7E3DC;
    }

    @media (max-width: 650px) {
        .block-container {
            padding: 1.3rem 1rem 2rem;
        }

        .hero-title {
            letter-spacing: -1px;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

header_left, header_right = st.columns([3, 2])

with header_left:
    st.markdown(
        '<div class="brand">Cine<span class="brand-accent">'
        'Match</span></div>',
        unsafe_allow_html=True
    )

with header_right:
    st.markdown(
        '<div style="text-align:right; color:#77746E; '
        'font-size:12px; padding-top:7px;">'
        'MOVIE DISCOVERY</div>',
        unsafe_allow_html=True
    )

st.divider()


# ---------- INTRODUCTION ----------

st.markdown(
    '<div class="eyebrow">A BETTER WAY TO FIND YOUR NEXT FILM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">Find a film worth watching.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-copy">'
    'Choose a movie you enjoy and discover five similar films '
    'based on their genres, story details and other content.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")


# ---------- MOVIE SELECTOR ----------

st.markdown(
    '<div class="section-heading">Choose your movie</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-copy">'
    'Select a title to explore recommendations.'
    '</div>',
    unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    "Movie title",
    movies["title"].values,
    label_visibility="collapsed",
    key="cinematch_movie"
)

st.write("")

recommend_clicked = st.button(
    "Find similar movies",
    use_container_width=True,
    key="cinematch_recommend"
)


# ---------- RESULTS ----------

if recommend_clicked:

    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie_name)

    st.write("")
    st.divider()

    st.markdown(
        '<div class="eyebrow">YOUR RECOMMENDATIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">Selected for you</div>',
        unsafe_allow_html=True
    )

    st.caption(f"Because you selected {selected_movie_name}")

    if not names:
        st.info("No recommendations found. Please try another movie.")

    else:
        columns = st.columns(5)

        for index, (name, poster) in enumerate(zip(names, posters)):
            with columns[index]:
                with st.container(border=True):
                    if poster:
                        st.image(poster, use_container_width=True)
                    else:
                        st.markdown(
                            '<div style="height:220px; display:flex; '
                            'align-items:center; justify-content:center; '
                            'background:#F1EFEA; color:#77746E; '
                            'border-radius:6px; font-size:12px;">'
                            'Poster unavailable</div>',
                            unsafe_allow_html=True
                        )

                    st.markdown(f"**{name}**")

                    st.caption(
                        f"RECOMMENDATION {index + 1:02d}"
                    )


# ---------- FOOTER ----------

st.write("")
st.divider()

st.markdown(
    '<div style="text-align:center; color:#89857E; '
    'font-size:12px; padding:8px 0;">'
    'CineMatch &nbsp;·&nbsp; Content-based movie recommendations'
    '</div>',
    unsafe_allow_html=True
)

# selected_movie_name = st.selectbox(
#     'How would you like to be connected ',
#     movies['title'].values
# )
#
# if st.button("Recommend"):
#     names,posters=recommend(selected_movie_name)

#to display posters from streamlit
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])