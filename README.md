# 🎬 Movie Recommender System

A content-based movie recommendation engine built with Python and Streamlit. This web application recommends 5 similar movies based on user selection and dynamically fetches official movie posters using a REST API.

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend/Deployment:** Streamlit, Streamlit Community Cloud
* **Machine Learning:** Scikit-learn (Cosine Similarity), Pandas, NumPy
* **External APIs:** TMDB API (via `requests` module)
* **Serialization:** Pickle

## ✨ Features
* **Content-Based Filtering:** Recommends movies based on similarity metrics calculated from movie metadata.
* **Dynamic Poster Fetching:** Integrates with the TMDB API to pull high-quality movie posters in real-time.
* **Responsive UI:** Clean, grid-based user interface built entirely in Python using Streamlit.

## 🧠 Technical Highlights
* **Memory Optimization:** Reduced the pickled cosine similarity matrix size by 50% (from 176MB to 88MB) by downcasting the data type from `float64` to `float32`, allowing for seamless version control and faster application boot times on cloud servers.
