from flask import Flask, render_template, request
import pickle
import requests
import numpy as np
import os


app = Flask(__name__)

movies = pickle.load(open("movies.pkl", "rb"))
similarity = np.load("similarity.npy", mmap_mode="r")

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

poster_cache = {}
recommend_cache = {}
details_cache = {}


def get_movie_details(movie_name):
    if movie_name in details_cache:
        return details_cache[movie_name]

    url = (
        f"https://api.themoviedb.org/3/search/movie"
        f"?api_key={TMDB_API_KEY}"
        f"&query={movie_name}"
    )

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("results"):
            movie = data["results"][0]

            details = {
                "title": movie_name,
                "rating": movie.get("vote_average", "N/A"),
                "overview": movie.get("overview", "No description available"),
                "release_date": movie.get("release_date", "Unknown"),
                "poster": (
                    "https://image.tmdb.org/t/p/w500" + movie.get("poster_path")
                    if movie.get("poster_path")
                    else "https://via.placeholder.com/300x450?text=No+Poster"
                )
            }

            details_cache[movie_name] = details
            return details

    except Exception as e:
        print("Details error:", e)

    fallback = {
        "title": movie_name,
        "rating": "N/A",
        "overview": "No description available",
        "release_date": "Unknown",
        "poster": "https://via.placeholder.com/300x450?text=No+Poster"
    }

    return fallback

def recommend(movie):
    try:
        if not movie:
            return [], []

        movie = movie.strip().lower()

       
        if movie in recommend_cache:
            return recommend_cache[movie]

       
        match = movies[movies["title"].str.lower().str.strip() == movie]

        if match.empty:
            print("Movie not found:", movie)
            return [], []

        movie_index = match.index[0]
        distances = similarity[movie_index]

        movie_list = np.argsort(distances)[::-1][1:6]

        recommended_movies = []
        recommended_posters = []
        recommended_details = []

        for i in movie_list:
            title = movies.iloc[i].title

            details = get_movie_details(title)

            recommended_movies.append(details)
            recommended_posters.append(details["poster"])

        recommend_cache[movie] = (recommended_movies, recommended_posters)

        return recommended_movies, recommended_posters

    except Exception as e:
        print("Recommendation error:", e)
        return [], []

@app.route("/", methods=["GET", "POST"])
def home():

    recommended_names = []
    recommended_posters = []

    movies_list = sorted(movies["title"].tolist())

    if request.method == "POST":
        selected_movie = request.form.get("movie")

        if selected_movie:
            recommended_names, recommended_posters = recommend(selected_movie)

    return render_template(
        "index.html",
        movies_list=movies_list,
        movie_names=recommended_names,
        posters=recommended_posters
    )

if __name__ == "__main__":
    app.run(debug=True)

