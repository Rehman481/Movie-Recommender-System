# Movie-Recommender-System
A Flask-based Movie Recommendation System that suggests similar movies using machine learning techniques such as cosine similarity. The system uses a precomputed similarity matrix and TMDB API integration to display movie posters, ratings, release dates, and descriptions in a clean web interface.
# 🎬 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black.svg)
![Machine Learning](https://img.shields.io/badge/ML-Content%20Based%20Filtering-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📸 Project Preview

### 🏠 Home Page
![Home](https://via.placeholder.com/900x400?text=Home+Page)

### 🎯 Recommendations
![Results](https://via.placeholder.com/900x400?text=Movie+Recommendations)

---

## 📌 About Project

This is a **Machine Learning based Movie Recommendation System** built using **Flask**.  
It recommends movies based on similarity scores and fetches posters using **TMDB API**.

---

## ✨ Features

- 🎬 Movie recommendation system
- 🔍 Search movies using dropdown
- 🤖 Content-based filtering (ML model)
- ⚡ Fast recommendations using similarity matrix
- 🖼️ Movie posters from TMDB API
- 🎨 Netflix-style responsive UI

---

## 🧠 How It Works

User selects a movie → System calculates similarity → Top 5 similar movies → Posters fetched from TMDB → Results displayed

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- Pandas 📊
- NumPy 🔢
- Scikit-learn 🤖
- HTML, CSS, Bootstrap 🎨
- TMDB API 🎬

---

## 📂 Project Structure

Movie-Recommender-System/
│
├── app.py
├── movies.pkl
├── similarity.npy
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
python app.py
