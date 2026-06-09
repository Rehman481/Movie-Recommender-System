
# 🎬 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black.svg)
![Machine Learning](https://img.shields.io/badge/ML-Content%20Based%20Filtering-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)


## 📌 About Project

This is a **Machine Learning based Movie Recommendation System** built using **Flask**.  
It recommends movies based on similarity scores and fetches posters using **TMDB API**.


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

## ⚙️ Installation

```bash
git clone https://github.com/Rehman481/Movie-Recommender-System.git
cd Movie-Recommender-System
pip install -r requirements.txt
python app.py


---
 📊 Dataset Used

This project uses movie metadata datasets for building the recommendation system:

- 🎥 TMDB 5000 Movies Dataset  
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

 
 📊 ML Model Details
Algorithm: Content-Based Filtering
Technique: Cosine Similarity
Dataset: Movie metadata
Optimization: Precomputed similarity matrix

 🚀 Future Improvements

🔥 Collaborative filtering
👤 User login system
⚡ Faster API caching
📱 Mobile optimization
🌐 Deploy with custom domain
